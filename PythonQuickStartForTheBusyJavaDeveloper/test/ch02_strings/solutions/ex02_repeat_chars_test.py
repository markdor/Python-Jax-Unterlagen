import pytest

from src.ch02_strings.solutions.ex02_repeat_chars import repeat_chars


# DISKUSSION: Wie expected / result angeben? => zweite Variante schöner
def test_repeat_chars_ABCD():
    assert "ABBCCCDDDD" == repeat_chars("ABCD")


def test_repeat_chars_ABCDEF():
    assert repeat_chars("ABCDEF") == "ABBCCCDDDDEEEEEFFFFFF"


# besser als parameterized test
@pytest.mark.parametrize("test_input,expected",
                         [("A", "A"),
                          ("AB", "ABB"),
                          ("ABCD", "ABBCCCDDDD"),
                          ("ABCDEF", "ABBCCCDDDDEEEEEFFFFFF")])
def test_repeat_chars(test_input, expected):
    assert repeat_chars(test_input) == expected
