def years_to_retirement(age, working_years):
    assert 18 <= age <= 65, 'age must be in range 18 - 65'
    assert 10 < working_years < 50, 'yeras must be in range 11 - 49'

    return 65 - age


years_to_retirement(70, 10)