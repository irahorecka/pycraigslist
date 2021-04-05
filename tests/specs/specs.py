"""
pycraigslist.tests.specs.specs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module stores static information for testing.
"""


class filters:
    """Build suite of filters used in searches by category."""

    housing = (
        {"min_bedrooms": 1, "max_price": 2000, "cats_ok": 1},
        {"max_price": 1000, "dogs_ok": True},
    )
