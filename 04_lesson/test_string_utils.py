import pytest
from string_utils import StringUtils

string_utils = StringUtils()


# Tests for capitalize()
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),  # starts with number
    ("", ""),  # empty string
    ("   ", "   "),  # whitespace only
    ("!test", "!test"),  # starts with special character
    ("42", "42"),  # numbers only
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# Tests for trim()
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("  hello world  ", "hello world  "),  # only left trim
    ("a", "a"),  # no whitespace
    ("    ", ""),  # all whitespace
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("skypro   ", "skypro   "),  # right whitespace remains
    ("", ""),  # empty string
    ("no_whitespace", "no_whitespace"),  # no whitespace at all
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


# Tests for contains()
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "k", True),
    ("SkyPro", "o", True),
    ("Hello World", " ", True),  # space
    ("12345", "3", True),  # number
    ("Multiple l letters", "l", True),  # multiple matches
])
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "U", False),
    ("", "a", False),  # empty string
    ("Hello", "h", False),  # case sensitive
    ("123", "4", False),  # number not present
    ("NoSpace", " ", False),  # space not present
])
def test_contains_negative(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


# Tests for delete_symbol()
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("Hello World", " ", "HelloWorld"),  # space removal
    ("ababab", "a", "bbb"),  # multiple removals
    ("112233", "2", "1133"),  # numbers
    ("Mississippi", "ss", "Miiippi"),  # overlapping patterns
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "X", "SkyPro"),  # symbol not present
    ("", "a", ""),  # empty string
    ("Hello", "h", "Hello"),  # case sensitive
    ("Same", "", "Same"),  # empty symbol
    ("NoChange", "123", "NoChange"),  # symbol not found
])
def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected