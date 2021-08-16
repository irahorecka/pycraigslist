"""
pycraigslist.exceptions
~~~~~~~~~~~~~~~~~~~~~~~

Contains the set of pycraigslist's exceptions.
"""


class MaximumRequestsError(Exception):
    """Exceeds maximum get requests."""


class InvalidFilterValue(ValueError):
    """Search filter has no or an invalid value."""

    def __init__(self, message, name, value):
        self.message = message
        self.name = name
        self.value = value
        super(InvalidFilterValue, self).__init__(message)
