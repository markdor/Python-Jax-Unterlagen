import datetime

# Generator
def date_range(start_date_incl, end_date_excl):
    # range kann nur mit ints umgehen, deswegen toordinal() nötig
    for day in range(start_date_incl.toordinal(), end_date_excl.toordinal()):
        yield datetime.date.fromordinal(day)


def all_friday13th(start_date_incl, end_date_excl):
    def is_friday(date):
        return date.isoweekday() == 5

    def is13th(date):
        return date.day == 13

    return [day.isoformat() for day in date_range(start, end)
            if is_friday(day) and is13th(day)]


start = datetime.date(2013, 1, 1)
end = datetime.date(2034, 1, 1)

print(all_friday13th(start, end))
