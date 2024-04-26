import pytest
from ch02_strings.solutions.ex07_is_anagram import is_anagram


@pytest.mark.parametrize("input1,input2",
                         [("Ampel", "Lampe"),
                          ("Ampel", "Palme"),
                          ("Palme", "Lampe")])
def test_is_anagram(input1, input2):
    assert is_anagram(input1, input2)

