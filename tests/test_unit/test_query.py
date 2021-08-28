"""
pycraigslist.tests.test_unit.test_query
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tests individual functions and class methods within the pycraigslist.query module.
"""


from pytest import mark, param

import pycraigslist


@mark.parametrize(
    ["input_", "expected"],
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
def test_parse_value(input_, expected):
    """Tests pycraigslist.query.filters.parse_filter_value function."""
    output = pycraigslist.query.filters.parse_filter_value(input_)
    if isinstance(output, list):
        assert output == expected
    else:
        assert list(output) == expected
