import pytest


def not_detected_test():
    assert sum([1, 2, 3]) == 6


def test_answer():
    assert sum([1, 2, 3]) == 6


@pytest.mark.parametrize("test_input,expected",
                         [("2 + 5", 7), ("2 ** 4", 16), ("6 * 9", 42)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected