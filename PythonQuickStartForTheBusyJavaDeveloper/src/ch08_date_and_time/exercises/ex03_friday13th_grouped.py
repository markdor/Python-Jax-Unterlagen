import datetime


def date_range(start_date, end_date):
    # TODO
    pass


def all_friday13th(start, end):
    # TODO
    pass


start = datetime.date(2013, 1, 1)
end = datetime.date(2016, 1, 1)

print(all_friday13th(start, end))

from itertools import groupby


def friday13th_grouped(start, end):
    # TODO
    pass

    result = {}

    # TODO
    pass

    return result


result = friday13th_grouped(start, end)
for year, fridays in result.items():
    print(year, ":", fridays)
