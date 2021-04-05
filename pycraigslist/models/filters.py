"""
pycraigslist.models.filters
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module parses and gets additional Craigslist query filters.
"""

from . import sessions


def get_addl_readable(url):
    """Gets additional Craigslist query filters in readable format."""
    filters = get_addl(url)
    for key, value in filters.copy().items():
        if isinstance(value, dict):
            # get only filter names
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


def parse(filters, search_filters):
    """Parses and validates url and filters using categorical search filters as
    template reference. Returns filters for requests.get params."""
    # iterate over a copy of filters
    for key, value in filters.copy().items():
        if key in ("searchNearby", "s"):
            # skip default filters found in all queries
            continue
        try:
            # substitute and remove key for url_key
            url_key = search_filters[key]["url_key"]
            filters[url_key] = parse_value(value)
            if url_key != key:
                # delete old key
                del filters[key]
        except KeyError:
            # some filters allow multiple values - assign all specified by user
            try:
                filters[key] = [
                    search_filters[key][parsed_val] for parsed_val in parse_value(value)
                ]
            except (KeyError, TypeError):
                raise ValueError("filter '%s' is or has a bad value" % key)

    return filters


def parse_value(filter_value):
    """Validates and further parses search filter values."""
    # returns filter value(s) as list
    if isinstance(filter_value, (float, str)):
        return [filter_value]
    # returns bool or int as int
    if isinstance(filter_value, (bool, int)):
        return [int(filter_value)]
    # recursively parses values if filter_value is an iterable
    return iter(parse_value(value)[0] for value in filter_value)
