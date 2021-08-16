"""
pycraigslist.tests.test_api.test_query
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tests instantiation, querying, and query output from pycraigslist .search
and .search_detail methods.
"""

import warnings
from functools import partial

from pytest import mark, param

import specs
import pycraigslist

# Make a tuple of zipped parameters for `test_query_filters`.
# I.e. pycraigslist.forsale will receive valid filters for the forsale category.
QUERY_FILTERS = tuple(zip(specs.obj.pycraigslist_parents, specs.filters.all_))
# Make a tuple of valid pycraigslist.api.* partial instances for `test_valid_instantiation`.
VALID_INSTANCES = tuple(
    partial(obj, **kwargs)
    for kwargs in specs.kwargs.valid
    for obj in specs.obj.pycraigslist_parents
)


@mark.parametrize("parent", specs.obj.pycraigslist_parents)
def test_dtype_search(parent):
    """Tests output datatype of search method."""
    listings = parent()
    if listings.count > 0:
        post = next(listings.search(limit=1))
        assert isinstance(post, dict)


@mark.parametrize("parent", specs.obj.pycraigslist_parents)
def test_content_search(parent):
    """Tests output content of search method."""
    listings = parent()
    if listings.count > 0:
        post = next(listings.search(limit=1))
        assert all(attr in post.keys() for attr in specs.content.post_content_std.keys())


@mark.parametrize("parent", specs.obj.pycraigslist_parents)
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


@mark.parametrize("parent", specs.obj.pycraigslist_parents)
def test_content_search_detail(parent):
    """Tests output content of search_detail method."""
    listings = parent()
    if listings.count > 0:
        # With include_body=True
        post_detail_w_body = next(listings.search_detail(limit=1, include_body=True))
        assert all(
            attr in post_detail_w_body.keys()
            for attr in specs.content.post_content_detail_body.keys()
        )

        # With include_body=False
        post_detail_wo_body = next(listings.search_detail(limit=1, include_body=False))
        assert all(
            attr in post_detail_wo_body.keys() for attr in specs.content.post_content_detail.keys()
        )

        # Without include_body kwarg --> default value is False.
        post_detail = next(listings.search_detail(limit=1))
        assert all(attr in post_detail.keys() for attr in specs.content.post_content_detail.keys())


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


@mark.parametrize(
    ["input", "expected"],
    [
        param("1", ["1"], id="String"),
        param(1.0, [1.0], id="Float"),
        param(True, [True], id="Boolean"),
        param(1, [1], id="Integer"),
        param(["1", "2"], ["1", "2"], id="List of integers"),
        param([1.0, 2.0], [1.0, 2.0], id="List of integers"),
        param([True, False], [True, False], id="List of integers"),
        param([1, 2], [1, 2], id="List of integers"),
        param(["1", 1, 1.0, True], ["1", 1, 1.0, True], id="Mixed list of types"),
    ],
)
def test_parse_value(input, expected):
    output = pycraigslist.query.filters.parse_value(input)
    if isinstance(output, list):
        assert output == expected
    else:
        assert list(output) == expected


@mark.parametrize(
    ["input", "modifications", "expected"],
    [
        param({"a": True}, {"a": False}, {"a": False}),
        param({"a": True, "b": True}, {"a": False}, {"a": False, "b": True}),
        param({"a": True}, {"b": True}, {"a": True, "b": True}),
    ],
)
def test_parse_arg_filters(input, modifications, expected):
    assert pycraigslist.query.filters.parse_arg_filters(input, **modifications) == expected
