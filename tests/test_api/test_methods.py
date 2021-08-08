"""
pycraigslist.tests.test_api.test_methods
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tests non-querying pycraigslist attributes, instance, and class methods.
"""

from pytest import mark

import specs

# Leave imported for `test_valid_subclasses_from_categories`.
import pycraigslist


@mark.parametrize("parent", specs.obj.pycraigslist_parents)
def test_dtype_get_filters(parent):
    """Tests instance method `get_filters()` returns dict object,
    i.e. a reference for its query filters."""
    listings = parent()
    assert isinstance(listings.get_filters(), dict)


@mark.parametrize("parent", specs.obj.pycraigslist_parents)
def test_dtype_get_categories(parent):
    """Tests class method `get_categories()` returns dict object,
    i.e. a reference for its subclass modules."""
    assert isinstance(parent.get_categories(), dict)


@mark.parametrize("parent", specs.obj.pycraigslist_parents)
def test_valid_subclasses_from_categories(parent):
    """Tests every subclass method suggested in `get_categories()` is a valid object."""
    parent_class_str = str(parent).split("'")[1]
    for subclass_key in parent.get_categories():
        # Throws AttributeError (i.e. fails test) if subclass isn't defined in pycraigslist/api.py.
        eval(f"{parent_class_str}.{subclass_key}")
    # Test passes if every suggested subclass of a parent class is valid.
    assert True


@mark.parametrize("parent", specs.obj.pycraigslist_parents)
def test_dtype_count(parent):
    """Tests attribute `count` returns int, i.e. the number of posts
    in the instance's query."""
    listings = parent()
    assert isinstance(listings.count, int)


@mark.parametrize("parent", specs.obj.pycraigslist_parents)
def test_dtype_url(parent):
    """Tests attribute `url` returns str object, i.e. the instance's
    query url."""
    listings = parent()
    assert isinstance(listings.url, str)
