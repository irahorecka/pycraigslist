from . import sessions


def get_addl_readable_filters(url):
    """ Gets additional Craigslist query filters in readable format. """
    filters = get_addl_filters(url)
    filters_iter = filters.copy()
    for key, value in filters_iter.items():
        if isinstance(value, dict):
            # get only the filter key bound to its numerical selector value
            filters[key] = list(value)

    return filters


def get_posts(url, filters, **kwargs):
    """ Gets every post on Craigslist as a dictionary with string values,
    provided a query url and filters. """
    # pass copy of filters to prevent manipulation by reference
    parsed_filters = parse_filters(url, filters.copy())
    # iterate through listings pages from a given search query
    search_html = sessions.get_html(url, params=parsed_filters)
    total_posts = get_total_posts(search_html)
    # there are 120 posts per listing page
    for search_page in range(int(total_posts / 120) + 1):
        search_page *= 120
        parsed_filters["s"] = search_page
        search_html = sessions.get_html(url, params=parsed_filters)

        yield from get_posts_in_search_page(search_html, **kwargs)


def parse_filters(url, filters):
    """ Takes query filters and parses them to match keyword value
    with appropriate integer value. """
    # TODO: can you include multiple filters per category?
    addl_filters = get_addl_filters(url)
    filters_iter = filters.copy()
    for key, value in filters_iter.items():
        if key in addl_filters:
            filters[key] = addl_filters[key][value]

    return filters


def get_addl_filters(url):
    """ Gets additional Craigslist query filters. """
    filters = {}
    search_html = sessions.get_html(url)
    for list_filter in search_html.find_all("div", class_="search-attribute"):
        filter_key = list_filter.attrs["data-attr"]
        filter_labels = list_filter.find_all("label")
        filters[filter_key] = {
            opt.text.strip(): opt.find("input").get("value") for opt in filter_labels
        }

    return filters


def get_total_posts(search_html_content):
    """ Gets total number of posts from Craigslist search page. """
    totalcount = search_html_content.find("span", {"class": "totalcount"})
    return int(totalcount.text) if totalcount else None


def get_posts_in_search_page(parsed_html, **kwargs):
    """ Yields posts content from Craigslist search HTML document
    given a page of Craigslist listings. """
    limit = kwargs["limit"]
    posts = parsed_html.find("ul", {"class": "rows"})
    for index, post in enumerate(posts.find_all("li", {"class": "result-row"}, recursive=False)):
        yield get_post_content(post, **kwargs)
        # search all listing if limit value is 0
        if index + 1 == limit:
            break


def get_post_content(post_html, **kwargs):
    """ Gets content from an individual post's HTML. """
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
    """ Parses site, area, and catgory from Craigslist query URL. """
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
    """ Gets additional post content from HTML document. """
    category = kwargs["category"]
    try:
        get_content = AddlContent.from_search_page[category]
        return get_content(post_html)
    except KeyError:
        return {}


# Though only containing one key and method, if a listings page is found to
# have extra post attributes, add appropriate selector and parsing method
# to this class.
class AddlContent:
    """ Gets additional post content from post's HTML and Craigslist
    search category. """

    from_search_page = {
        "apa": lambda post: AddlContent.parse_housing(
            post.find("span", {"class": "housing"}).contents
        )
        if post.find("span", {"class": "housing"})
        else ""
    }

    @staticmethod
    def parse_housing(contents):
        """ Parses additional content in apartments / housing for rent. """
        housing_attr = {}
        try:
            content = contents[0]
        except IndexError:
            content = []
        # this assumes no bedroom is > 99
        if "br" in content:
            housing_attr["bedrooms"] = str(
                int(content[content.find("br") - 2 : content.find("br")])
            )
        # for ft2 - assuming no area is greater than 10^10 ft2
        if "ft" in content:
            housing_attr["area-ft2"] = str(
                int(content[content.find("ft") - 10 : content.find("ft")])
            )
        # for m2 - assuming no area is greater than 10^10 m2
        if "m" in content:
            housing_attr["area-m2"] = str(int(content[content.find("m") - 10 : content.find("m")]))

        return housing_attr
