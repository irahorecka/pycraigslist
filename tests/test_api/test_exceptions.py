"""
pycraigslist.tests.test_api.test_exceptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tests proper exception raises from pycraigslist.api.* instances.
"""

from functools import partial

import pytest
from pytest import mark

import specs

# Make a tuple of invalid pycraigslist.api.* partial instances for `test_invalid_instantiation`.
INVALID_INSTANCES = tuple(
    partial(obj, **kwargs)
    for kwargs in specs.kwargs.invalid
    for obj in specs.obj.pycraigslist_parents
)


@mark.parametrize("invalid_instance", INVALID_INSTANCES)
def test_invalid_instantiation(invalid_instance):
    """Tests invalid instantiation of pycraigslist.api.* class using invalid kwargs.
    Invalid kwargs could pertain to the following: bad site key, bad area key, bad filter key.
    All invalid instantiation should result in a ValueError."""
    with pytest.raises(ValueError):
        invalid_instance()
