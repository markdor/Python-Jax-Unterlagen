import pytest

from src.ch02_strings.solutions.ex03_vowels import remove_vowel, replace_vowel


@pytest.mark.parametrize("test_input,expected",
                         [("Es gibt viel zu entdecken!", "s gbt vl z ntdckn!"),
                          ("PYTHON INTRO BY MICHAEL", "PYTHN NTR BY MCHL")])
def test_remove(test_input, expected):
    assert remove_vowel(test_input) == expected


@pytest.mark.parametrize("test_input,replacement,expected",
                         [("Es gibt viel zu entdecken!", "XX", "XXs gXXbt vXXXXl zXX XXntdXXckXXn!"),
                          ("PYTHON INTRO BY MICHAEL", "-", "PYTH-N -NTR- BY M-CH--L")])
def test_replace(test_input, replacement, expected):
    assert replace_vowel(test_input, replacement) == expected
