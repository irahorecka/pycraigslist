"""
pycraigslist.query.filters
~~~~~~~~~~~~~~~~~~~~~~~~~~

Handles parsing of Craigslist query filters.
"""

from pycraigslist.constants import region
from pycraigslist.exceptions import InvalidFilterValue
from pycraigslist.query import sessions


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


def parse_filters_to_params(reference_filters, filters, **kwargs):
    """Parses and validates filters, using categorical query filters as
    a reference. Returns filters as parameters for an HTTP request."""
    # Merge `filters` with `**kwargs`.
    # `**kwargs` will override `filters` if matching key exists.
    filters = {**filters, **kwargs} if isinstance(filters, dict) else kwargs
    # Iterate over a copy of filters.
    for key, value in filters.copy().items():
        try:
            # Substitute and remove key for url_key.
            url_key = reference_filters[key]["url_key"]
            filters[url_key] = parse_filter_value(value)
            if url_key != key:
                # Delete old key.
                del filters[key]
        except KeyError:
            # Some filters allow multiple values - assign all as specified by caller.
            try:
                filters[key] = [
                    reference_filters[key][parsed_val] for parsed_val in parse_filter_value(value)
                ]
            except (KeyError, TypeError) as error:
                raise InvalidFilterValue(
                    "either '%s' is an invalid filter or '%s' is a bad value for '%s'"
                    % (key, value, key),
                    key,
                    value,
                ) from error

    # Join default parameters for every filter.
    return {**{"searchNearby": 1, "s": 0}, **filters}


def parse_filter_value(value):
    """Validates and further parses query filter values."""
    # Returns filter value(s) as list.
    if isinstance(value, (float, str)):
        return [value]
    # Returns bool or int as int.
    if isinstance(value, (bool, int)):
        return [int(value)]
    # Recursively parses values if `value` is an iterable.
    return iter(parse_filter_value(value)[0] for value in value)


def validate_region(site, area):
    """Validates user input for site and area. Raises ValueError if bad input(s)."""
    if site not in region.sites:
        raise ValueError("'%s' is not a valid Craigslist site" % site)
    if area:
        if site not in region.areas:
            raise ValueError("site '%s' does not have an area" % site)
        if area not in region.areas.get(site, set()):
            raise ValueError("'%s' is not a valid Craigslist area for site '%s'" % (area, site))
