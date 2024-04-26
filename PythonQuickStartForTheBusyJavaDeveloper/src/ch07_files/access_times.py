import datetime
import os


def seconds_to_time(seconds):
    return datetime.datetime.fromtimestamp(seconds)


print("created", seconds_to_time(os.path.getctime("personenliste.txt")))
print("modified", seconds_to_time(os.path.getmtime("personenliste.txt")))
print("accessed", seconds_to_time(os.path.getatime("personenliste.txt")))
