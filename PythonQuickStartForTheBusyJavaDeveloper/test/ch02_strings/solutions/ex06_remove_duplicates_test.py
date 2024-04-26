import pytest

from ch02_strings.solutions.ex06_remove_duplicate_chars import remove_duplicates


@pytest.mark.parametrize("test_input,expected",
                         [("lalamlam", "lam"),
                          ("bananas", "bans")])
def test_remove_duplicates(test_input, expected):
    assert remove_duplicates(test_input) == expected
