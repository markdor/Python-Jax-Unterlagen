import datetime


def get_week_day(my_date):
    return my_date.strftime('%A')


def print_week_day(date):
   print(date.isoformat() + " is a " + get_week_day(date))


christmas_eve = datetime.date(2019, 12, 24)
december1st = datetime.date(2019, 12, 1)
december31st = datetime.date(2019, 12, 31)

print_week_day(christmas_eve)
print_week_day(december1st)
print_week_day(december31st)
