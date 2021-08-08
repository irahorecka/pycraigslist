"""
pycraigslist.query.search
~~~~~~~~~~~~~~~~~~~~~~~~~

Gets and parses posts from a Craigslist query.
"""

import re

from pycraigslist.query import sessions


def fetch_posts(url, filters, **kwargs):
    """Yields every post from a Craigslist query as a dictionary with string values;
    provided a URL and query filters from the caller."""
    total_post_count = get_total_post_count(url, filters)
    # Return empty search if total_post_count cannot be found in search page.
    if total_post_count == 0:
        return ()

    limit = kwargs["limit"]
    # Choose lesser number of posts if comparable.
    if not limit or total_post_count < limit:
        limit = total_post_count
    yield from fetch_posts_to_limit(url, filters, limit, **kwargs)


def get_total_post_count(url, filters):
    """Gets total number of posts from Craigslist URL and parameters."""
    search_html = next(sessions.yield_html(url, params=filters))
    total_count = search_html.find("span", {"class": "totalcount"})
    return 0 if total_count is None else int(total_count.text)


def fetch_posts_to_limit(url, filters, num_posts, **kwargs):
    """Exhaustively yields posts' content (up to num_posts) from Craigslist
    URL and filters."""
    # Find number of search pages - there are 120 posts per page.
    num_pages = int(num_posts / 120) + 1 if num_posts % 120 != 0 else int(num_posts / 120)
    # Container to hold appending iterables
    zip_iter = []
    for page_num in range(num_pages):
        # Get first post's post index in a search page.
        # E.g. third page first post is 240, i.e. it is the 240th post in the query.
        filters["s"] = page_num * 120
        zip_iter.append((url, filters.copy(), filters["s"]))

    # Unzip for threading requests.
    search_urls, page_filters, start_idxs = zip(*zip_iter)
    search_pages = sessions.yield_html(search_urls, params=page_filters)
    for idx, html in enumerate(search_pages):
        yield from (
            fetch_posts_from_page(html, start_idx=start_idxs[idx], stop_idx=num_posts, **kwargs)
        )


def fetch_posts_from_page(page_html, start_idx, stop_idx, **kwargs):
    """Yields posts' content from a page of Craigslist listings (HTML content)."""
    # We want country and region to precede all keys.
    post_json = get_post_country_region(page_html)
    posts = page_html.find("ul", {"class": "rows"})
    for idx, post in enumerate(posts.find_all("li", {"class": "result-row"}, recursive=False)):
        # Country and region attributes are post-agnostic - merge post_json with post content.
        yield {**post_json, **get_post_content(post, **kwargs)}
        # Adjust for true post count idx.
        idx += start_idx
        if idx + 1 == stop_idx:
            # Reached post limit.
            break


def get_post_country_region(page_html):
    """Gets post's country and region from a Craigslist listings' page
    (HTML content)."""
    # Javascript syntax for areaCountry and areaRegion.
    js_country_re = re.compile('var areaCountry = "(.*?)";')
    js_region_re = re.compile('var areaRegion = "(.*?)";')
    # JSON syntax for areaCountry and areaRegion.
    json_country_re = re.compile('areaCountry: "(.*?)",')
    json_region_re = re.compile('areaRegion: "(.*?)",')

    post_country_region = {}
    scripts = page_html.find_all("script")
    for script in scripts:
        if script.string is None:
            continue
        # If country pattern matches, region pattern will match.
        if bool(js_country_re.findall(script.string)):
            post_country_region["country"] = js_country_re.findall(script.string)[0]
            post_country_region["region"] = js_region_re.findall(script.string)[0]
            break
        if bool(json_country_re.findall(script.string)):
            post_country_region["country"] = json_country_re.findall(script.string)[0]
            post_country_region["region"] = json_region_re.findall(script.string)[0]
            break

    return post_country_region


def get_post_content(post_html, **kwargs):
    """Gets content from an individual post's HTML."""
    # Prepare bs4 html for parse.
    header_link = post_html.find("a", {"class": "hdrlnk"})
    neighborhood = post_html.find("span", {"class": "result-hood"})
    price = post_html.find("span", {"class": "result-price"})
    repost_of = post_html.attrs.get("data-repost-of")
    time = post_html.find("time")
    if time:
        datetime = time.attrs["datetime"]
    else:
        pl = post_html.find("span", {"class": "pl"})
        datetime = pl.text.split(":")[0].strip() if pl else None

    # Parse bs4 html.
    post_id = post_html.attrs["data-pid"]
    post_repost_of = repost_of or ""
    post_last_updated = datetime
    post_title = header_link.text
    post_neighborhood = neighborhood.text.strip()[1:-1] if neighborhood else ""
    post_price = price.text if price else ""
    post_url = header_link.attrs["href"]
    post_site, post_area, post_category = parse_url_subdomains(post_url)

    # Construct post content.
    post_content = {
        "site": post_site,
        "area": post_area,
        "category": post_category,
        "id": post_id,
        "repost_of": post_repost_of,
        "last_updated": post_last_updated,
        "title": post_title,
        "neighborhood": post_neighborhood,
        "price": post_price,
        "url": post_url,
    }
    # If additional content is available, concat to post content.
    return {**post_content, **get_addl_content(post_html, **kwargs)}


def parse_url_subdomains(url):
    """Parses site, area, and category from Craigslist query URL."""
    parsed_url = url.split("https://")[1].split(".")
    parsed_suburl = parsed_url[2].split("/")
    site = parsed_url[0]
    # `parsed_suburl` will have len == 5 if query has no area.
    # `parsed_suburl` will have len == 6 if query has area.
    if len(parsed_suburl) == 5:
        area = ""
        category = parsed_suburl[1]
    else:
        area = parsed_suburl[1]
        category = parsed_suburl[2]
    return site, area, category


def get_addl_content(post_html, **kwargs):
    """Gets additional post content from post's HTML row."""
    category = kwargs["category"]
    try:
        get_content = AddlContent.search[category]
        return get_content(post_html)
    except KeyError:
        return {}


class AddlContent:
    """Gets additional post content from post's HTML row."""

    # Though currently containing one key and method, if a listings page is found to
    # have extra post attributes than standard, add appropriate selector and parsing
    # method to this class.

    search = {
        "apa": lambda post: AddlContent.parse_housing(
            post.find("span", {"class": "housing"}).contents
        )
        if post.find("span", {"class": "housing"})
        else {}
    }

    @staticmethod
    def parse_housing(contents):
        """Parses additional content in apartments / housing for rent."""
        try:
            content = contents[0]
        except IndexError:
            # Return empty dict if no additional housing attributes found.
            return {}

        housing_attr = {}
        # This assumes no bedroom is > 99.
        if "br" in content:
            br_idx = content.find("br")
            housing_attr["bedrooms"] = str(int(content[br_idx - 2 : br_idx]))
        # For ft2 - assuming no area is greater than 10^10 ft2.
        if "ft" in content:
            ft_idx = content.find("ft")
            housing_attr["area-ft2"] = str(int(content[ft_idx - 10 : ft_idx]))
        # For m2 - assuming no area is greater than 10^10 m2.
        if "m" in content:
            m_idx = content.find("m")
            housing_attr["area-m2"] = str(int(content[m_idx - 10 : m_idx]))

        return housing_attr
