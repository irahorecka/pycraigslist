"""
pycraigslist.tests.test_api.test_query
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tests instantiation, querying, and query output from pycraigslist .search
and .search_detail methods.
"""

import warnings
from functools import partial

import pytest
from pytest import mark

import params
import pycraigslist

# Make a tuple of zipped parameters for `test_query_filters`.
# I.e. pycraigslist.forsale will receive valid filters for the forsale category.
QUERY_FILTERS = tuple(zip(params.obj.pycraigslist_parents, params.filters.all_))
# Make a tuple of valid pycraigslist.api.* partial instances for `test_valid_instantiation`.
VALID_INSTANCES = tuple(
    partial(obj, **kwargs)
    for kwargs in params.kwargs.valid
    for obj in params.obj.pycraigslist_parents
)


@mark.parametrize("parent", params.obj.pycraigslist_parents)
def test_dtype_search(parent):
    """Tests output datatype of search method."""
    listings = parent()
    if listings.count > 0:
        post = next(listings.search(limit=1))
        assert isinstance(post, dict)


@mark.parametrize("parent", params.obj.pycraigslist_parents)
def test_content_search(parent):
    """Tests output content of search method."""
    listings = parent()
    if listings.count > 0:
        post = next(listings.search(limit=1))
        assert all(attr in post for attr in params.content.post_content_std)


@mark.parametrize("parent", params.obj.pycraigslist_parents)
def test_dtype_search_detail(parent):
    """Tests output datatype of search_detail method."""
    listings = parent()
    if listings.count > 0:
        # With include_body=True
        post_detail_w_body = next(listings.search_detail(limit=1, include_body=True))
        assert isinstance(post_detail_w_body, dict)

        # With include_body=False
        post_detail_wo_body = next(listings.search_detail(limit=1, include_body=False))
        assert isinstance(post_detail_wo_body, dict)

        # Without include_body kwarg --> default value is False.
        post_detail = next(listings.search_detail(limit=1))
        assert isinstance(post_detail, dict)


@mark.parametrize("parent", params.obj.pycraigslist_parents)
def test_content_search_detail(parent):
    """Tests output content of search_detail method."""
    listings = parent()
    if listings.count > 0:
        # With include_body=True
        post_detail_w_body = next(listings.search_detail(limit=1, include_body=True))
        assert all(attr in post_detail_w_body for attr in params.content.post_content_detail_body)

        # With include_body=False
        post_detail_wo_body = next(listings.search_detail(limit=1, include_body=False))
        assert all(attr in post_detail_wo_body for attr in params.content.post_content_detail)

        # Without include_body kwarg --> default value is False.
        post_detail = next(listings.search_detail(limit=1))
        assert all(attr in post_detail for attr in params.content.post_content_detail)


@mark.parametrize("parent", params.obj.pycraigslist_parents)
def test_impossible_query(parent):
    """Tests queries that will (almost) always yield no posts."""
    listings = parent(query="@@ this is likely an impossible query @@")
    # Posts' count of 0 is expected for a query with no posts.
    assert listings.count == 0
    with pytest.raises(StopIteration):
        # Stop iteration is expected for a query with no posts.
        next(listings.search())


@mark.parametrize(["parent", "filters"], QUERY_FILTERS)
def test_query_filters(parent, filters):
    """Tests search filters plugged into query returns valid pycraigslist
    datatype (i.e. dict obj). Tests every parent category with their respective
    query filters."""
    for filter_ in filters:
        try:
            post = next(parent(filters=filter_).search(limit=10))
            assert isinstance(post, dict)
        except StopIteration:
            # No posts for query and a stop iteration is expected; however, throw warning.
            warnings.warn(
                UserWarning(
                    "encountered StopIteration for filters %s. Adjust if issue persists." % filter_
                )
            )
            assert True


@mark.parametrize("valid_instance", VALID_INSTANCES)
def test_valid_instantiation(valid_instance):
    """Tests proper instantiation of pycraigslist.api.* instances using valid kwargs."""
    assert type(valid_instance()).__bases__[0] == pycraigslist.base.BaseAPI


def test_filter_override():
    """Tests the proper overriding of the `filter` keyword dictionary values with those
    provided as a keyword argument."""
    filters = {
        "bicycle_frame_material": "steel",
    }
    # 'aluminum' should override 'steel' when constructing an instance with
    # matching filter keywords.
    bicycles = pycraigslist.forsale.bia(filters=filters, bicycle_frame_material="aluminum")
    assert next(bicycles.search_detail(limit=1))["bicycle_frame_material"] == "aluminum"
