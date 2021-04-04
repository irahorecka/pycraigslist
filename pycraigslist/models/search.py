import re
from . import sessions


def fetch_posts(url, filters, **kwargs):
    """Yields every post on Craigslist as a dictionary with string values,
    provided a url and query filters."""
    search_html = next(sessions.yield_html(url, params=filters))
    total_post_count = get_total_post_count(search_html)
    # return empty search if total_post_count cannot be found in search page
    if total_post_count is None:
        return ()

    limit = kwargs["limit"]
    # choose lesser number of posts if comparable
    if not limit or total_post_count < limit:
        limit = total_post_count
    yield from fetch_posts_to_limit(url, filters, limit, **kwargs)


def get_total_post_count(search_html_content):
    """Gets total number of posts from Craigslist search page."""
    totalcount = search_html_content.find("span", {"class": "totalcount"})
    return int(totalcount.text) if totalcount else None


def fetch_posts_to_limit(url, filters, num_posts, **kwargs):
    """Exhaustively yield post contents from Craigslist url and filters
    up to num_posts."""
    # find number of pages for search - there are 120 posts per page
    num_pages = int(num_posts / 120) + 1 if num_posts % 120 != 0 else int(num_posts / 120)
    # container to hold appending iterables
    zip_iter = []
    for page_num in range(num_pages):
        # get first post's index in a search page
        start_index = page_num * 120
        filters["s"] = start_index
        zip_iter.append((url, filters.copy(), start_index))

    # unzip for threading requests
    search_urls, page_filters, start_posts = zip(*zip_iter)
    search_pages = sessions.yield_html(search_urls, params=page_filters)
    for idx, html in enumerate(search_pages):
        yield from (
            fetch_posts_from_page(html, start_idx=start_posts[idx], stop_idx=num_posts, **kwargs)
        )


def fetch_posts_from_page(page_html, start_idx, stop_idx, **kwargs):
    """Yields posts content from a page (HTML doc) of Craigslist listings."""
    posts = page_html.find("ul", {"class": "rows"})
    for idx, post in enumerate(posts.find_all("li", {"class": "result-row"}, recursive=False)):
        # we want country and region to precede all keys
        post_json = get_post_country_region(page_html)
        post_json.update(get_post_content(post, **kwargs))
        yield post_json
        # adjust for true post count idx
        idx += start_idx
        if idx + 1 == stop_idx:
            # reach post limit
            break


def get_post_country_region(page_html):
    """Gets post's country and region from a page (HTML doc) of
    Craigslist listings."""
    post_country_region = {}
    script = page_html.find("script", type="text/javascript")

    country_pattern = re.compile('var areaCountry = "(.*?)";')
    region_pattern = re.compile('var areaRegion = "(.*?)";')
    post_country_region["country"] = country_pattern.findall(script.string)[0]
    post_country_region["region"] = region_pattern.findall(script.string)[0]

    return post_country_region


def get_post_content(post_html, **kwargs):
    """Gets content from an individual post's HTML."""
    # prep bs4 html for parse
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

    # parse bs4 html
    post_id = post_html.attrs["data-pid"]
    post_repost_of = "" if not repost_of else repost_of
    post_last_updated = datetime
    post_title = header_link.text
    post_neighborhood = neighborhood.text.strip()[1:-1] if neighborhood else ""
    post_price = price.text if price else ""
    post_url = header_link.attrs["href"]
    post_site, post_area, post_category = parse_url_subdomains(post_url)

    # construct post content
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
    # if additional content is available, concat to post content
    post_content.update(get_addl_content(post_html, **kwargs))

    return post_content


def parse_url_subdomains(url):
    """Parses site, area, and catgory from Craigslist query URL."""
    parsed_url = url.split("https://")[1].split(".")
    parsed_suburl = parsed_url[2].split("/")
    site = parsed_url[0]
    # parsed_suburls will have len == 5 if query has no area
    # len == 6 if query has area
    if len(parsed_suburl) == 5:
        area = ""
        category = parsed_suburl[1]
    else:
        area = parsed_suburl[1]
        category = parsed_suburl[2]

    return site, area, category


def get_addl_content(post_html, **kwargs):
    """Gets additional post content from HTML doc."""
    category = kwargs["category"]
    try:
        get_content = AddlContent.from_search_page[category]
        return get_content(post_html)
    except KeyError:
        return {}


class AddlContent:
    """Gets additional post content from post's HTML doc and Craigslist
    search category."""

    # Though only containing one key and method, if a listings page is found to
    # have extra post attributes, add appropriate selector and parsing method
    # to this class.

    from_search_page = {
        "apa": lambda post: AddlContent.parse_housing(
            post.find("span", {"class": "housing"}).contents
        )
        if post.find("span", {"class": "housing"})
        else ""
    }

    @staticmethod
    def parse_housing(contents):
        """Parses additional content in apartments / housing for rent."""
        try:
            content = contents[0]
        except IndexError:
            # if no additional housing attributes found
            return {}

        housing_attr = {}
        # this assumes no bedroom is > 99
        if "br" in content:
            br_idx = content.find("br")
            housing_attr["bedrooms"] = str(int(content[br_idx - 2 : br_idx]))
        # for ft2 - assuming no area is greater than 10^10 ft2
        if "ft" in content:
            ft_idx = content.find("ft")
            housing_attr["area-ft2"] = str(int(content[ft_idx - 10 : ft_idx]))
        # for m2 - assuming no area is greater than 10^10 m2
        if "m" in content:
            m_idx = content.find("m")
            housing_attr["area-m2"] = str(int(content[m_idx - 10 : m_idx]))

        return housing_attr
