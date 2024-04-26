import pytest

from ch99_testing.well_formed_braces import check_braces


@pytest.mark.parametrize("input, expected, hint",
                         [("(())", True, "ok"),
                          ("()()", True, "ok"),
                          ("(()))((())", False, "nicht sauber geschachtelt"),
                          ("(()", False, "keine passende Klammerung"),
                          (")()", False, "startet mit schliessender Klammer")])
def test_check_braces(input, expected, hint):
    assert check_braces(input) == expected
