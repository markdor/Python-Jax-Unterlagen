import datetime
import locale
import calendar

def now():
    return datetime.datetime.now()


now_ = now()
#now2 = now()


# datetime(year, month, day)
date_no_time_set = datetime.datetime(2020, 11, 23)

# datetime(year, month, day, hour, minute, second, microsecond)
date_and_time = datetime.datetime(2017, 11, 28, 23, 55, 59, 342380)
print("numbers:", date_and_time)

date_and_time = datetime.datetime(2017, calendar.Month.NOVEMBER, 28, 23, 55, 59, 342380)
date_and_time = datetime.datetime(2017, calendar.NOVEMBER, 28, 23, 55, 59, 342380)
print("with constants", date_and_time)

sunday_afternoon = datetime.datetime(2021, 6, 13, 16, 52, 59)
print("year =", sunday_afternoon.year)
print("month =", sunday_afternoon.month)
print("day =", sunday_afternoon.day)
print("weekday() =", sunday_afternoon.weekday())
print("isoweekday() =", sunday_afternoon.isoweekday())

print("date() =", sunday_afternoon.date())
print("time() =", sunday_afternoon.time())
print("ts =", sunday_afternoon.timestamp())

datetime_from_ts = datetime.datetime.fromtimestamp(43211234)
pure_ts = datetime_from_ts.timestamp()
print(datetime_from_ts.timestamp())

start = datetime.datetime(2021, 2, 7, 10, 10, 10)
end = datetime.datetime(2021, 2, 8, 11, 12, 13)
print("end - start =", end - start)
print(type(end - start))
#print("end + start =", end + start)

td1 = datetime.timedelta(weeks=2, days=3, hours=5, seconds=6)
td2 = datetime.timedelta(days=7, hours=8, minutes=9, seconds=10)
print(td1 - td2)
print(td1 + td2)

michas_birthday = datetime.date(1971, 2, 7)
print(michas_birthday + td2 * 2)

############################# DATE ##############################


def today():
    return datetime.date.today()

date_from_iso = datetime.date.fromisoformat('2020-11-23')

today = datetime.date.today()
print("Current year:", date_from_iso.year)
print("Current month:", date_from_iso.month)
print("Current day:", date_from_iso.day)
print("weekday():", date_from_iso.weekday())
print("isoweekday():", date_from_iso.isoweekday())


def get_week_day(date):
    return date.strftime('%A')


def day_of_month(date):
    return date.day


def day_of_year(date):
    return date.timetuple().tm_yday


def day_of_year_2(date):
    return date.strftime('%j')


print(get_week_day(date_from_iso))
print(day_of_month(date_from_iso))
print(day_of_year(date_from_iso))
print(day_of_year_2(date_from_iso))


print((datetime.date(2012, 3, 1) - datetime.date(2012, 2, 1)).days)
print((datetime.date(2014, 3, 1) - datetime. date(2014, 2, 1)).days)

def length_of_month(month, year):
    start = datetime.date(year, month, 1)
    month += 1
    if month > 12:
        year += 1
        month = 1

    end = datetime.date(year, month, 1)
    return (end - start).days


def length_of_year(year):
    start = datetime.date(year, 1, 1)
    end = datetime.date(year + 1, 1, 1)
    return (end - start).days


import calendar

print("2012 is leap?", calendar.isleap(2012))


date_from_ts = datetime.date.fromtimestamp(34774300)
print(date_from_ts)

christmas_eve_20 = datetime.date.fromisoformat('2020-12-24')
print(christmas_eve_20.toordinal())


######################## TIME ######################################

def current_time():
    return datetime.datetime.now().time()


print("current_time() =", current_time())

# time(hour, minute, second)
print(datetime.time(11, 28, 45))

# time(hour, minute, second, microsecond)
print(datetime.time(11, 28, 45, 6789))


##########################################################

date_string = "14 July, 1979"

date_object = datetime.datetime.strptime(date_string, "%d %B, %Y")
print("Parsed:", date_object)


date_string = "14. Juli 1979"
locale.setlocale(locale.LC_ALL, 'de_DE')
localized_date_object = datetime.datetime.strptime(date_string, "%d. %B %Y")
locale.setlocale(locale.LC_ALL, locale.getdefaultlocale())
print("Parsed with locale:", localized_date_object)


def get_localized_month(month_nr, desired_locale):
    current_locale = locale.getlocale()
    locale.setlocale(locale.LC_ALL, desired_locale)
    month_name = datetime.datetime.strptime(month_nr, "%m").strftime("%B")
    locale.setlocale(locale.LC_ALL, current_locale)
    return month_name


for i in range(1, 13):
    print(get_localized_month(str(i), 'de_DE'),
          get_localized_month(str(i), 'fr_FR'),
          get_localized_month(str(i), 'it_IT'))


def get_localized_weekday(weekday_nr, desired_locale):
    current_locale = locale.getlocale()
    locale.setlocale(locale.LC_ALL, desired_locale)
    weekday_name = datetime.datetime.strptime(weekday_nr, "%d").strftime("%A")
    locale.setlocale(locale.LC_ALL, current_locale)
    return weekday_name


for i in range(1, 8):
    print(get_localized_weekday(str(i), 'de_DE'),
          get_localized_weekday(str(i), 'fr_FR'),
          get_localized_weekday(str(i), 'it_IT'),
          get_localized_weekday(str(i), 'es_ES'))