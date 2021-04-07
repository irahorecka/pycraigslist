"""
pycraigslist.tests.test_api.test_filters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tests the `filters` parameter in pycraigslist parent classes.
"""

import warnings
from pytest import mark

import specs

# make a tuple of zipped parameters for `test_query_filters`
query_filters_params = tuple(zip(specs.obj.pycraigslist_parents, specs.filters.all_))


@mark.parametrize(["parent", "filters"], query_filters_params)
def test_query_filters(parent, filters):
    """Tests search filters plugged into query returns valid pycraigslist
    datatype (i.e. dict obj). Tests every parent category with their respective
    query filters."""
    for filter_ in filters:
        try:
            post = next(parent(filters=filter_).search(limit=10))
            assert isinstance(post, dict)
        except StopIteration:
            # No posts for query and a stop iteration is expected;
            # however, throw warning.
            warnings.warn(
                UserWarning(
                    "encountered StopIteration for filters %s. Adjust if issue persists." % filter_
                )
            )
            assert True
