"""
pycraigslist.query.search_detail
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Adds details to posts from a Craigslist query.
"""

from pycraigslist.query import sessions


def fetch_detailed_posts(standard_posts, **kwargs):
    """Fetches additional details from every post in `standard_posts`."""
    # Expand all post values fetched from standard search and link with post ID.
    posts = {post["id"]: post for post in standard_posts}
    urls = [post["url"] for post in posts.values()]
    # Parameters are not required when querying an individual post.
    params = [{} for _ in urls]
    # Yield every post's HTML content.
    htmls = sessions.yield_html(urls, params=params)
    kwargs["reference_filters"] = invert_filters(kwargs["reference_filters"])

    # Yield detailed posts to caller.
    for html in htmls:
        post_details = get_post_details(html, **kwargs)
        try:
            # Because we're dealing with asynchronous requests, link post details
            # to standard post content by post ID.
            yield {**posts[post_details["id"]], **post_details}
        except KeyError:
            # If post ID in details doesn't match post IDs from general search.
            pass


def invert_filters(reference_filters):
    """Inverts reference query filters for a faster look-up time downstream."""
    inverted_filters = {}
    for key, value in reference_filters.items():
        try:
            # From {"cats_ok": {"url_key": "pets_cat", "value": 1, "attr": "cats are ok - purrr"},}
            # To {"cats are ok - purrr": {"cats_ok": "true"},}
            inverted_filters[value["attr"]] = {key: "true"}
        except KeyError:
            # For filters with multiple values.
            # From {'auto_bodytype': ['bus', 'convertible', ... ],}
            # To {'bus': 'auto_bodytype', 'convertible': 'auto_bodytype', ... ,}
            if isinstance(value, dict):
                inverted_filters.update({child_value: key for child_value in value})

    return inverted_filters


def get_post_details(post_content, **kwargs):
    """Gets additional post details as dictionary."""
    addl_detail = {}
    addl_detail.update(get_id(post_content))
    addl_detail.update(get_geotag(post_content))
    addl_detail.update(get_address(post_content))
    addl_detail.update(get_attrs(post_content, **kwargs))
    include_body = kwargs.get("include_body")
    if include_body in (True, 1):
        addl_detail.update(get_body(post_content))
    return addl_detail


def get_id(post_content):
    """Gets post ID from posts's HTML content."""
    post_infos = post_content.find_all("p", {"class": "postinginfo"})
    id_ = {"id": ""}
    for post_info in post_infos:
        if post_info.string is None:
            continue
        post_info_str = post_info.string.lower()
        if "id: " in post_info_str:
            id_["id"] = post_info_str.split("id: ").pop()
            break

    return id_


def get_geotag(post_content):
    """Gets latitude and longitude from post's HTML content."""
    post_map = post_content.find("div", {"id": "map"})
    geotag = {"lat": "", "lon": ""}
    if post_map is not None:
        geotag["lat"] = post_map.attrs["data-latitude"]
        geotag["lon"] = post_map.attrs["data-longitude"]
    return geotag


def get_address(post_content):
    """Gets address from post's HTML content."""
    post_address = post_content.find("div", {"class": "mapaddress"})
    address = {"address": ""}
    if post_address is not None:
        address["address"] = post_address.text
    return address


def get_body(post_content):
    """Gets body from post's HTML content."""
    post_body = post_content.find("section", {"id": "postingbody"})
    body = {"body": ""}
    if post_body is not None:
        # Remove elements with null attributes.
        post_body_text = (
            getattr(element, "text", element)
            for element in post_body
            if not getattr(element, "attrs", None)
        )
        # Squelch post_body_text to str.
        body["body"] = str("".join(post_body_text).strip())
    return body


def get_attrs(post_content, **kwargs):
    """Gets additional attributes from post's HTML content."""
    reference_filters = kwargs["reference_filters"]
    # Attributes without a recognizable ID will be appended to "misc".
    attrs = {"misc": []}
    for attr_key in get_attr_keys(post_content):
        # Add to attrs !! BY REFERENCE !!.
        parse_attrs(attrs, attr_key, reference_filters)

    return attrs


def get_attr_keys(post_content):
    """Gets attribute reference keys from post's HTML content."""
    for attribute in post_content.find_all("p", {"class": "attrgroup"}):
        for attr in attribute.find_all("span"):
            attr_text = attr.text.strip()
            if attr_text:
                yield attr_text.lower()


def parse_attrs(post_attrs, attr_key, reference_filters):
    """Parses attributes using reference query filters. Adds parsed
    attributes by reference to attributes collection (post_attrs)."""
    if attr_key in reference_filters:
        if isinstance(reference_filters[attr_key], dict):
            # E.g. update with {"cats_ok": "true"} from {"cats are ok - purrr": {"cats_ok": "true"},}
            post_attrs.update(reference_filters[attr_key])
        else:
            # Update with attribute value.
            post_attrs.update({reference_filters[attr_key]: attr_key})
    elif ":" in attr_key:
        # Some attr keys are delimited by ':' - parse it to dict and update.
        # These attr keys are commonly separated by whitespaces and backslashes - replace with '_'.
        key_ = attr_key.split(":")[0].strip().replace(" / ", " ").replace(" ", "_")
        attr_ = attr_key.split(":")[1].strip()
        post_attrs.update({key_: attr_})
    else:
        # attr key not found in filter - append to list of anonymous attributes.
        post_attrs["misc"].append(attr_key)
