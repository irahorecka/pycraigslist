"""
pycraigslist.base
~~~~~~~~~~~~~~~~~

This module handles all communication from the user to the Craigslist API.
"""

import urllib
from . import models
from .utils import parse_limit


class BaseAPI:
    """Base class for interfacing with the Craigslist API."""

    category = ""
    search_filters = {}

    def __init__(self, site="sfbay", area="", filters=None, **kwargs):
        self.site = site
        self.area = area
        self.search_filters = {**self.search_filters, **models.filters.get_addl(self._base_url)}
        self.filters = {"searchNearby": 1, "s": 0}
        # **kwargs will override filters if matching key exists
        if isinstance(filters, dict):
            self.filters.update(filters)
        self.filters.update(**kwargs)
        # parse self.filters to construct valid HTTP parameters
        self.filters = models.filters.parse(self.filters, self.search_filters)

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
            self.search(limit=limit), filters=self.search_filters, include_body=include_body
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

    @classmethod
    def get_filters(cls):
        """Gets readable Craigslist query filters for given class.
        The intention is to provide user with valid filter keys and values,
        therefore the returned dictionary is catered for ease of interpretation."""
        category = cls.__name__ if not cls.category else cls.category
        # set sfbay classified as default craigslist search url
        category_url = "https://sfbay.craigslist.org/search/%s" % category
        readable_filters = {
            key: "..." if value["value"] is None else "True/False"
            for key, value in cls.search_filters.items()
        }
        readable_filters.update(models.filters.get_addl_readable(category_url))

        return readable_filters


class ParentMethods:
    """Provides parent classes with additional class methods."""

    @classmethod
    def get_categories(cls):
        """Gets valid Craigslist categories of instance."""
        from . import filters

        return filters.category.get(cls.__name__)
