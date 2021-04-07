"""
pycraigslist.base
~~~~~~~~~~~~~~~~~

Handles communication between the User and Craigslist.
"""

import urllib
from . import models
from .utils import parse_limit


class BaseAPI:
    """Base class for interfacing with the Craigslist API."""

    category = ""
    # Standard query filters that are permitted within category
    query_filters = {}

    def __init__(self, site="sfbay", area="", filters=None, **kwargs):
        self.site = site
        self.area = area
        # Get additional filters joined with standard filters
        self.all_query_filters = {**self.query_filters, **models.filters.get_addl(self._base_url)}
        # Get parsed filters to use as HTTP parameters
        self.filters = models.filters.parse(filters, self.all_query_filters, **kwargs)

    @parse_limit
    def search(self, limit=None):
        """Yields Craigslist posts as dictionary."""
        yield from models.search.fetch_posts(
            self._base_url, self.filters, category=self.category, limit=limit
        )

    @parse_limit
    def search_detail(self, limit=None, include_body=False):
        """Yields detailed Craigslist posts as dictionary."""
        yield from models.search_detail.fetch_posts(
            self.search(limit=limit), include_body=include_body, ref_filters=self.all_query_filters
        )

    @property
    def count(self):
        """Gets approximate number of Craigslist posts."""
        return models.search.get_total_post_count(self._base_url, self.filters)

    @property
    def url(self):
        """Builds full Craigslist query URL."""
        return "%s?%s" % (self._base_url, urllib.parse.urlencode(self.filters, doseq=True))

    @property
    def _base_url(self):
        """Builds standard Craigslist query URL."""
        if not self.area:
            return "https://%s.craigslist.org/search/%s" % (self.site, self.category)
        return "https://%s.craigslist.org/search/%s/%s" % (self.site, self.area, self.category)

    def get_filters(self):
        """Gets Craigslist query filters in a readable format."""
        readable_filters = {
            key: "..." if value["value"] is None else "True/False"
            for key, value in self.query_filters.items()
        }
        readable_filters.update(models.filters.get_addl_readable(self._base_url))

        return readable_filters


class ParentMethods:
    """Provides parent classes with additional class methods."""

    @classmethod
    def get_categories(cls):
        """Gets valid Craigslist categories of instance."""
        from . import filters

        return filters.category.get(cls.__name__)
