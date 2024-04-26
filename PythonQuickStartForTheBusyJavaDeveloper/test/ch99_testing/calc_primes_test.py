import pytest

from ch99_testing.calc_primes import calc_primes_up_to


def input_and_expected():
    return [(2, [2]),
            (3, [2, 3]),
            (10, [2, 3, 5, 7]),
            (15, [2, 3, 5, 7, 11, 13]),
            (25, [2, 3, 5, 7, 11, 13, 17, 19, 23])]


@pytest.mark.parametrize("n, expected",
                         input_and_expected())
def test_calc_primes_up_to(n, expected):
    assert calc_primes_up_to(n) == expected
