"""
pycraigslist.tests.specs.specs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module stores static information for testing.
"""
import pycraigslist


class filters:
    """Build suite of filters used in searches by category."""

    housing = (
        {"min_bedrooms": 1, "max_price": 2000, "cats_ok": 1},
        {"max_price": 1000, "dogs_ok": True},
    )


pycraigslist_parents = [
    pycraigslist.community,
    pycraigslist.events,
    pycraigslist.forsale,
    pycraigslist.gigs,
    pycraigslist.housing,
    pycraigslist.jobs,
    pycraigslist.resumes,
    pycraigslist.services,
]
