"""
pycraigslist.utils
~~~~~~~~~~~~~~~~~~

Provides utility functions for pycraigslist.base.
"""

from functools import wraps


def parse_limit(method):
    """Wrapper to parse 'limit' kwarg in base.BaseAPI.search
    and base.BaseAPI.search_detail methods."""

    @wraps(method)
    def wrapper(*args, **kwargs):
        limit = kwargs.get("limit")
        # Yield method if limit is valid.
        if limit is None or isinstance(limit, int) and limit >= 0:
            yield from method(*args, **kwargs)
        elif not isinstance(limit, int):
            raise TypeError("'limit' must be of type 'int'")
        else:
            raise ValueError("'limit' must be greater than / equal to 0")

    return wrapper
