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
    """Tests pycraigslist.query.filters.parse_value function."""
    output = pycraigslist.query.filters.parse_value(input_)
    if isinstance(output, list):
        assert output == expected
    else:
        assert list(output) == expected


@mark.parametrize(
    ["input_", "modifications", "expected"],
    [
        param({"a": True}, {"a": False}, {"a": False}),
        param({"a": True, "b": True}, {"a": False}, {"a": False, "b": True}),
        param({"a": True}, {"b": True}, {"a": True, "b": True}),
    ],
)
def test_parse_arg_filters(input_, modifications, expected):
    """Tests pycraigslist.query.filters.parse_arg_filters function."""
    assert pycraigslist.query.filters.parse_arg_filters(input_, **modifications) == expected
