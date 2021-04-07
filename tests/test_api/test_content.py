"""
pycraigslist.tests.test_api.test_content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tests content from pycraigslist .search and .search_detail methods.
"""

from pytest import mark

import specs


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

        # Without include_body kwarg --> default value is False
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

        # Without include_body kwarg --> default value is False
        post_detail = next(listings.search_detail(limit=1))
        assert all(attr in post_detail.keys() for attr in specs.content.post_content_detail.keys())
