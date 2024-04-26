import pytest

from ch02_strings.solutions.ex04_reverse_string import reverse_string


@pytest.mark.parametrize("test_input,expected",
                         [("ABC", "CBA"),
                          ("ABCDEFGHI", "IHGFEDCBA")])
def test_reverse_string(test_input, expected):
    assert reverse_string(test_input) == expected
