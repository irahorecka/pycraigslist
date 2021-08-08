"""
pycraigslist.query.filters
~~~~~~~~~~~~~~~~~~~~~~~~~~

Handles parsing of Craigslist query filters.
"""

from pycraigslist.query import sessions
from pycraigslist.filters import region


def get_addl_filters_readable(url):
    """Gets additional Craigslist query filters in readable format."""
    addl_filters = get_addl_filters(url)
    for key, value in addl_filters.copy().items():
        if isinstance(value, dict):
            # Get only filter names.
            # E.g. ['apartment', 'condo'] from {'apartment': '1', 'condo': '2'}
            addl_filters[key] = list(value)
    return addl_filters


def get_addl_filters(url):
    """Gets additional Craigslist query filters."""
    # Additional filters constitute niche filters for a category.
    # E.g. 'rent_period' is an additional filter for apartments / housing for rent.
    addl_filters = {}
    search_html = next(sessions.yield_html(url))

    for filter_item in search_html.find_all("div", {"class": "search-attribute"}):
        filter_key = filter_item.attrs["data-attr"]
        filter_labels = filter_item.find_all("label")
        addl_filters[filter_key] = {
            opt.text.strip(): opt.find("input").get("value") for opt in filter_labels
        }

    return addl_filters


def parse_filters(filters, query_filters, **kwargs):
    """Parses and validates URL and filters using categorical query filters as
    template reference. Returns filters for requests.get params."""
    filters = parse_arg_filters(filters, **kwargs)
    # Iterate over a copy of filters.
    for key, value in filters.copy().items():
        try:
            # Substitute and remove key for url_key.
            url_key = query_filters[key]["url_key"]
            filters[url_key] = parse_value(value)
            if url_key != key:
                # Delete old key.
                del filters[key]
        except KeyError:
            # Some filters allow multiple values - assign all specified by user.
            try:
                filters[key] = [query_filters[key][parsed_val] for parsed_val in parse_value(value)]
            except (KeyError, TypeError):
                raise ValueError("filter '%s' is or has a bad value" % key)

    # Join default parameters for every filter.
    return {**{"searchNearby": 1, "s": 0}, **filters}


def parse_arg_filters(filters, **kwargs):
    """Parses and returns a dictionary from `filters` and **kwargs."""
    query_filters = {}
    # **kwargs will override filters if matching key exists.
    if isinstance(filters, dict):
        query_filters.update(filters)
    return {**query_filters, **kwargs}


def parse_value(filter_value):
    """Validates and further parses query filter values."""
    # Returns filter value(s) as list.
    if isinstance(filter_value, (float, str)):
        return [filter_value]
    # Returns bool or int as int.
    if isinstance(filter_value, (bool, int)):
        return [int(filter_value)]
    # Recursively parses values if filter_value is an iterable.
    return iter(parse_value(value)[0] for value in filter_value)


def validate_region(site, area):
    """Validates user input for site and area. Raises ValueError if bad input(s)."""
    if site not in region.sites:
        raise ValueError("'%s' is not a valid Craigslist site" % site)
    if area and area not in region.areas.get(site, set()):
        raise ValueError("'%s' is not a valid Craigslist area for site '%s'" % (area, site))
