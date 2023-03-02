"""
pycraigslist.exceptions
~~~~~~~~~~~~~~~~~~~~~~~

Contains the set of pycraigslist's exceptions.
"""

from requests.exceptions import ConnectionError


class HTTPError(Exception):
    """An HTTP error occurred."""

    def __init__(self, status_code, detail):
        self.status_code = status_code
        self.detail = detail
        super().__init__("%s %s" % (self.status_code, self.detail))


class InvalidFilterValue(ValueError):
    """Filter is not recognized or has an invalid value."""

    def __init__(self, message, name, value):
        self.message = message
        self.name = name
        self.value = value
        super().__init__(message)
