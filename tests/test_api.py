"""
pycraigslist.tests.test_api
~~~~~~~~~~~~~~~~~~~~~~~~~~~

A pytest-based test file to test the pycraigslist API.
"""

from pytest import mark

import specs
import pycraigslist
from pycraigslist import models


@mark.parametrize("filters", specs.filters.housing)
def test_filters(filters):
    """Test search filters return valid pycraigslist response."""
    post = next(pycraigslist.housing.apa(filters=filters).search(limit=10))
    assert isinstance(post, dict)


@mark.parametrize("limit", [2983, 1121, 38, 1928])
def test_limits(limit):
    """Test number of posts always equal the search limit, or the maximum
    posts of page if exceeded by limit."""
    apa = pycraigslist.housing.apa()
    len_posts = len([post for post in apa.search(limit=limit)])

    filters = {"searchNearby": 1, "s": 0}
    expected_len = models.search.get_total_post_count(apa.url, filters)

    if expected_len > len_posts:
        assert len_posts == limit
    else:
        assert len_posts == expected_len


@mark.parametrize("limit", [400, 383, 3, 121])
def test_detail_limits(limit):
    """Test number of detailed posts always equal the search limit, or the maximum
    posts of page if exceeded by limit."""
    cta = pycraigslist.forsale.cta()
    len_posts = len([post for post in cta.search_detail(limit=limit)])

    filters = {"searchNearby": 1, "s": 0}
    expected_len = models.search.get_total_post_count(cta.url, filters)

    if expected_len > len_posts:
        assert len_posts == limit
    else:
        assert len_posts == expected_len
