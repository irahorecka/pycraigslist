"""
pycraigslist.models.search_detail
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module gets and parses detailed posts from a Craigslist query.
"""

from . import sessions


def fetch_posts(general_search, **kwargs):
    """Fetches details from every post in general_search."""
    # Yield all post values from general search and link with post id
    posts = {post["id"]: post for post in general_search}
    posts_url = [post["url"] for post in posts.values()]
    params = [{} for _ in posts_url]
    # Get every post's HTML content
    post_htmls = sessions.yield_html(posts_url, params=params)
    kwargs["filters"] = invert_filters(kwargs["filters"])

    # Yield detailed posts to caller
    for html in post_htmls:
        post_details = get_post_details(html, **kwargs)
        try:
            # Because we're dealing with asynchronous requests, link post details
            # to standard post content by post id
            yield {**posts[post_details["id"]], **post_details}
        except KeyError:
            # If post ID in details doesn't match post IDs from general search
            pass


def invert_filters(search_filters):
    """Inverts search filters for a faster look-up time."""
    inv_filters = {}
    for key, value in search_filters.items():
        try:
            # From {"cats_ok": {"url_key": "pets_cat", "value": 1, "attr": "cats are ok - purrr"},}
            # To {"cats are ok - purrr": {"cats_ok": "true"},}
            inv_filters[value["attr"]] = {key: "true"}
        except KeyError:
            # For filters with multiple values
            # From {'auto_bodytype': ['bus', 'convertible', ... ],}
            # To {'bus': 'auto_bodytype', 'convertible': 'auto_bodytype', ... ,}
            if isinstance(value, dict):
                inv_filters.update({child_value: key for child_value in value})

    return inv_filters


def get_post_details(post_content, **kwargs):
    """Gets additional post details as dictionary."""
    addl_detail = {}
    addl_detail.update(get_post_id(post_content))
    addl_detail.update(get_geotag(post_content))
    addl_detail.update(get_address(post_content))
    addl_detail.update(get_post_attrs(post_content, **kwargs))
    include_body = kwargs.get("include_body")
    if include_body in (True, 1):
        addl_detail.update(get_body(post_content))

    return addl_detail


def get_post_id(post_content):
    """Gets post ID from posts's HTML content."""
    post_infos = post_content.find_all("p", {"class": "postinginfo"})
    post_attr = {"id": ""}
    for post_info in post_infos:
        if post_info.string is None:
            continue
        post_info_str = post_info.string.lower()
        if "id: " in post_info_str:
            post_attr["id"] = post_info_str.split("id: ").pop()
            break

    return post_attr


def get_geotag(post_content):
    """Gets geotag from post's HTML content."""
    post_map = post_content.find("div", {"id": "map"})
    geotag_attr = {"lat": "", "lon": ""}
    if post_map is not None:
        geotag_attr["lat"] = post_map.attrs["data-latitude"]
        geotag_attr["lon"] = post_map.attrs["data-longitude"]

    return geotag_attr


def get_address(post_content):
    """Gets address from post's HTML content."""
    post_address = post_content.find("div", {"class": "mapaddress"})
    address_attr = {"address": ""}
    if post_address is not None:
        address_attr["address"] = post_address.text

    return address_attr


def get_body(post_content):
    """Gets body from post's HTML content."""
    post_body = post_content.find("section", id="postingbody")
    body_attr = {"body": ""}
    if post_body is not None:
        # Remove elements with null attributes
        post_body_text = (
            getattr(element, "text", element)
            for element in post_body
            if not getattr(element, "attrs", None)
        )
        # Squelch post_body_text to str
        body_attr["body"] = str("".join(post_body_text).strip())

    return body_attr


def get_post_attrs(post_content, **kwargs):
    """Gets attributes from post's HTML content."""
    filters = kwargs["filters"]
    # Attributes without a recognizable ID will be appended to "misc"
    post_attrs = {"misc": []}
    for attr in get_attrs(post_content):
        # Add to post_attrs by reference
        parse_attrs(post_attrs, attr, filters)

    return post_attrs


def get_attrs(post_content):
    """Gets attribute keys from post's HTML content."""
    for attribute in post_content.find_all("p", {"class": "attrgroup"}):
        for attr in attribute.find_all("span"):
            attr_text = attr.text.strip()
            if attr_text:
                yield attr_text.lower()


def parse_attrs(post_attrs, attr, filters):
    """Parses attributes using search filters as reference. Adds parsed
    attributes to attributes collection (post_attrs) by reference."""
    if attr in filters:
        if isinstance(filters[attr], dict):
            # E.g. update with {"cats_ok": "true"} from {"cats are ok - purrr": {"cats_ok": "true"},}
            post_attrs.update(filters[attr])
        else:
            # Update with attribute value
            post_attrs.update({filters[attr]: attr})
    elif ":" in attr:
        # Some attr key, value are delimited by ':' - parse it to dict and update
        key_ = attr.split(":")[0].strip()
        attr_ = attr.split(":")[1].strip()
        post_attrs.update({key_: attr_})
    else:
        # attr not found in filter - append to list of anonymous attributes
        post_attrs["misc"].append(attr)
