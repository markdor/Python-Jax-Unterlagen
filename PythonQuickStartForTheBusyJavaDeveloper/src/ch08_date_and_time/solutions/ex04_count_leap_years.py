import calendar


def count_leap_years(start, end):
    count = 0
    for year in range(start, end):
        if calendar.isleap(year):
            count += 1
    return count


print(count_leap_years(2010, 2019))
print(count_leap_years(2000, 2019))


def count_leap_years_2(start, end):
    return sum([1 for year in range(start, end) if calendar.isleap(year)])


print(count_leap_years_2(2010, 2019))
print(count_leap_years_2(2000, 2019))
