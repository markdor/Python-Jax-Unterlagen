import datetime


def calc_length_of_month(month, year):
    start = datetime.date(year, month, 1)

    month += 1
    if month > 12:
        year += 1
        month = 1

    end = datetime.date(year, month, 1)

    return (end - start).days


def print_calendar(month, year):
    print("Mo Di Mi Do Fr Sa So ")

    cur = datetime.date(year, month, 1)

    first_in_month = cur.isoweekday()

    skip_till_first_day_of_month(first_in_month)

    current_week_day = first_in_month
    length_of_month = calc_length_of_month(month, year)

    for i in range (1, length_of_month + 1):
        print("%0.2d" % i, end=" ")

        if current_week_day == 0:
            print()

        current_week_day = calc_next_week_day(current_week_day)

    fill_from_month_end_to_sunday(current_week_day)

    # letzter Tag nicht Sonntag, dann Umbruch
    if current_week_day != 1:
        print()


def calc_next_week_day(current_week_day):
    return (current_week_day + 1) % 7


def skip_till_first_day_of_month(first_in_month):
    # start on Monday
    current_week_day = 1
    while current_week_day != first_in_month:
        print(".. ", end="")
        current_week_day = calc_next_week_day(current_week_day)


def fill_from_month_end_to_sunday(current_week_day):
    next_week_day = current_week_day
    while next_week_day != 1:
        print("-- ", end="")
        next_week_day = calc_next_week_day(next_week_day)
    print()


print_calendar(4, 2020)
print_calendar(5, 2020)
print_calendar(6, 2020)

print_calendar(12, 2020)
print_calendar(1, 2021)
print_calendar(2, 2021)

print_calendar(2, 2020)
