from . import sessions


def get_addl_readable(url):
    """Gets additional Craigslist query filters in readable format."""
    filters = get_addl(url)
    filters_iter = filters.copy()
    for key, value in filters_iter.items():
        if isinstance(value, dict):
            # get only the filter key bound to its numerical selector value
            # e.g. ['apartment', 'condo'] from {'apartment': '1', 'condo': '2'}
            filters[key] = list(value)

    return filters


def get_addl(url):
    """Gets additional Craigslist query filters."""
    # additional filters constitute niche filters for a category
    # e.g. 'rent_period' is an additional filter for apartments / housing for rent
    filters = {}
    search_html = next(sessions.yield_html(url))

    for filter_item in search_html.find_all("div", class_="search-attribute"):
        filter_key = filter_item.attrs["data-attr"]
        filter_labels = filter_item.find_all("label")
        filters[filter_key] = {
            opt.text.strip(): opt.find("input").get("value") for opt in filter_labels
        }

    return filters


def parse(url, filters, search_filters):
    """Parses and validates url and filters using search_filters as template reference.
    Returns filters for GET request parameter `params`."""
    addl_filters = get_addl(url)

    # iterate over a copy of filters
    for key, value in filters.copy().items():
        try:
            if key in addl_filters:
                # addl_filters allow multiple values - assign all specified by user
                filters[key] = [addl_filters[key][parsed_val] for parsed_val in parse_value(value)]
            else:
                # working with standard filters
                try:
                    # substitute and remove key for url_key
                    url_key = search_filters.get(key)["url_key"]
                    del filters[key]
                # thrown when attempting to subscript 'searchNearby' or 's'
                except TypeError:
                    url_key = key
                filters[url_key] = parse_value(value)

        # bad value
        except (KeyError, ValueError) as bad_value:
            raise ValueError("%s is not a valid value for filter '%s'" % (bad_value, key))

    return filters


def parse_value(filter_value):
    """Validates and further parses search filter values."""
    # returns filter value(s) as list
    if isinstance(filter_value, (float, str)):
        return [filter_value]
    # returns bool or int as int
    if isinstance(filter_value, (bool, int)):
        return [int(filter_value)]
    try:
        # recursively parses values if filter_value is an iterable
        return iter(parse_value(value) for value in filter_value)
    except TypeError:
        # overall a bad object, e.g. a class without and iterable
        raise ValueError(filter_value)
