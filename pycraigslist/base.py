from . import models


class BaseAPI:
    """Base class for interfacing with the Craigslist API."""

    category = ""
    search_filters = {}

    def __init__(self, site="sfbay", area="", filters=None, **kwargs):
        self.site = site
        self.area = area
        self.filters = {"searchNearby": 1, "s": 0}
        # **kwargs will override filters if matching key exists
        if isinstance(filters, dict):
            self.filters.update(filters)
        self.filters.update(**kwargs)

    def search(self, limit=None):
        """Yields Craigslist posts as dictionary."""
        parsed_filters = models.filters.parse(self.url, self.filters, self.search_filters)
        if limit is None or isinstance(limit, int) and limit >= 0:
            yield from models.search.yield_posts(
                self.url, parsed_filters, category=self.category, limit=limit
            )

        elif not isinstance(limit, int):
            raise TypeError("'limit' must be of type 'int'")
        else:
            raise ValueError("'limit' must be greater than / equal to 0")

    @property
    def url(self):
        """Builds Craigslist query URL."""
        if not self.area:
            return "https://%s.craigslist.org/search/%s" % (self.site, self.category)
        return "https://%s.craigslist.org/search/%s/%s" % (self.site, self.area, self.category)

    @classmethod
    def get_filters(cls):
        """Gets readable Craigslist query filters for given class.
        The intention is to provide user with valid filter keys and values,
        therefore the returned dictionary is catered for ease of interpretation."""
        category = cls.__name__ if not cls.category else cls.category
        # default sfbay classified as craigslist search url
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
