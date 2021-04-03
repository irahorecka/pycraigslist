from pytest import mark

import specs
import pycraigslist
from pycraigslist import models


@mark.parametrize("filters", specs.filters.housing)
def test_filters(filters):
    """Test search filters return valid pycraigslist response."""
    post = next(pycraigslist.housing.apa(filters=filters).search(limit=10))
    assert isinstance(post, dict)


@mark.parametrize("limit", [400, 383, 1928, 3, 2983, 939, 1121, 38, 929, 3, 1887])
def test_limits(limit):
    """Test number of posts always equal the search limit, or the maximum
    posts of page if exceeded by limit."""
    apa = pycraigslist.housing.apa()
    filters = {"searchNearby": 1, "s": 0}
    len_posts = len([post for post in apa.search(limit=limit)])
    search_html = next(models.sessions.yield_html(apa.url, params=filters))
    expected_len = models.search.get_total_post_count(search_html)

    if expected_len > len_posts:
        assert len_posts == limit
    else:
        assert len_posts == expected_len
