import datetime


################# Generator

def date_range(start_date, end_date):
    for day in range(start_date.toordinal(), end_date.toordinal()):
        yield datetime.date.fromordinal(day)


def all_friday13th(start, end):
    def is_friday(date):
        return date.isoweekday() == 5

    def is13th(date):
        return date.day == 13

    return [day.isoformat() for day in date_range(start, end)
            if is_friday(day) and is13th(day)]


start = datetime.date(2013, 1, 1)
end = datetime.date(2016, 1, 1)

all_friday13th_ = all_friday13th(start, end)
print(all_friday13th_)

grouped = {}
for friday in all_friday13th_:
    extract_year = lambda isodate: isodate[0:4]

    key = extract_year(friday)
    if key in grouped:
        grouped[key] += [friday]
    else:
        grouped[key] = [friday]

print(grouped)



####################################################
from itertools import groupby


def friday13th_grouped(start, end):
    all_friday13th_ = all_friday13th(start, end)

    result = {}

    extract_year = lambda isodate: isodate[0:4]
    for key, group in groupby(all_friday13th_, extract_year):
        members = list(group)
        result.update({key: members})

    return result


result = friday13th_grouped(start, end)
for year, fridays in result.items():
    print(year, ":", fridays)
