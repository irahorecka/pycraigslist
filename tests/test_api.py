"""
pycraigslist.tests.test_api
~~~~~~~~~~~~~~~~~~~~~~~~~~~

A pytest-based test file to test the pycraigslist API.
"""

from pytest import mark

import specs
import pycraigslist


@mark.parametrize("filters", specs.filters.housing)
def test_filters(filters):
    """Tests search filters return valid pycraigslist response."""
    post = next(pycraigslist.housing.apa(filters=filters).search(limit=10))
    assert isinstance(post, dict)


@mark.parametrize("limit", [2983, 1121, 38, 1928])
def test_limits(limit):
    """Tests number of posts always equal the search limit, or the maximum
    posts of page if exceeded by limit."""
    apa = pycraigslist.housing.apa()
    len_posts = len([post for post in apa.search(limit=limit)])
    expected_len = apa.count

    if expected_len > len_posts:
        assert len_posts == limit
    else:
        assert len_posts == expected_len


@mark.parametrize("limit", [83, 121, 3, 34])
def test_detail_limits(limit):
    """Tests number of detailed posts always equal the search limit, or the maximum
    posts of page if exceeded by limit."""
    cta = pycraigslist.forsale.cta()
    len_posts = len([post for post in cta.search_detail(limit=limit)])
    expected_len = cta.count

    if expected_len > len_posts:
        assert len_posts == limit
    else:
        assert len_posts == expected_len


@mark.parametrize("parent", specs.pycraigslist_parents)
def test_datatype_search(parent):
    """Tests output datatype of search method."""
    listings = parent()
    if listings.count > 0:
        assert isinstance(next(listings.search(limit=1)), dict)


@mark.parametrize("parent", specs.pycraigslist_parents)
def test_datatype_search_detal(parent):
    """Tests output datatype of search_detail method."""
    listings = parent()
    if listings.count > 0:
        assert isinstance(next(listings.search_detail(limit=1, include_body=True)), dict)
