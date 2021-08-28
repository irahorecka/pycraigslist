"""
pycraigslist.base
~~~~~~~~~~~~~~~~~

Handles communication between the User and Craigslist.
"""

import urllib
from pycraigslist import constants, query
from pycraigslist.utils import parse_limit


class BaseAPI:
    """Base class for interfacing with the Craigslist API."""

    category = ""
    # Standard query filters that are permitted within category.
    query_filters = {}

    def __init__(self, site="sfbay", area="", filters=None, **kwargs):
        # Validate site and area values from caller.
        query.validate_region(site, area)
        self.site = site
        self.area = area
        # Join additional filters with standard filters.
        self.query_filters_all = {
            **self.query_filters,
            **query.get_addl_filters(self.base_url),
        }
        # Parse filters to get HTTP parameters.
        self.params = query.parse_filters_to_params(self.query_filters_all, filters, **kwargs)

    @parse_limit
    def search(self, limit=None):
        """Yields Craigslist posts as dictionary."""
        yield from query.fetch_posts(
            self.base_url, self.params, category=self.category, limit=limit
        )

    @parse_limit
    def search_detail(self, limit=None, include_body=False):
        """Yields detailed Craigslist posts as dictionary."""
        yield from query.fetch_detailed_posts(
            self.search(limit=limit),
            include_body=include_body,
            reference_filters=self.query_filters_all,
        )

    @property
    def count(self):
        """Gets approximate number of Craigslist posts."""
        return query.get_total_post_count(self.base_url, self.params)

    @property
    def url(self):
        """Builds full Craigslist query URL."""
        return "%s?%s" % (
            self.base_url,
            urllib.parse.urlencode(self.params, doseq=True),
        )

    @property
    def base_url(self):
        """Builds standard Craigslist query URL."""
        if not self.area:
            return "https://%s.craigslist.org/search/%s" % (self.site, self.category)
        return "https://%s.craigslist.org/search/%s/%s" % (
            self.site,
            self.area,
            self.category,
        )

    def get_filters(self):
        """Gets Craigslist query filters in a readable format."""
        readable_filters = {
            key: "..." if value["value"] is None else "True/False"
            for key, value in self.query_filters.items()
        }
        return {**readable_filters, **query.get_addl_filters_readable(self.base_url)}


class ParentMethods:
    """Provides parent classes with additional class methods."""

    @classmethod
    def get_categories(cls):
        """Gets valid Craigslist categories of instance."""
        return constants.category.get(cls.__name__)
