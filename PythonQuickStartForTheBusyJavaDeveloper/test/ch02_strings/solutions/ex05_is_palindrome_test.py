import pytest

from ch02_strings.solutions.ex05_is_palindrome import is_palindrome, is_palindrome_rec

def input_parameters():
    return [("Sophie", False),
            ("OTTO", True),
            ("DrehMalAmHerd", True),
            ("Dreh Mal Am Herd", False)]


@pytest.mark.parametrize("test_input,expected",
                         input_parameters())
def test_reverse_string(test_input, expected):
    assert is_palindrome(test_input) == expected


@pytest.mark.parametrize("test_input,expected",
                         input_parameters())
def test_reverse_string_rec(test_input, expected):
    assert is_palindrome_rec(test_input) == expected



