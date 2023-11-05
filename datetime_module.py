import datetime

# definitions: naive vs. aware datetimes
# naive: don't have enough info to determine things like time zones, daylight savings
# aware: These are able to determine their time zones, daylight savings

d = datetime.date(2023, 10, 18)
print(d)

# what is today's date?
tday = datetime.date.today()
print(tday)
# what day of the week is it?
# print(tday.weekday())  # Monday 0; Sunday 6
print(tday.isoweekday()) #Monday 1; Sunday 7

# time deltas (differences between dates/times)
tdelta = datetime.timedelta(days=7)
# what will the date be in 7 days?
print(tday + tdelta)
# what was the date 7 days ago?
print(tday - tdelta)

# Adding/Subtracting dates and timedeltas
# date2 = date1 + timedelta
# timedelta = date1 + date2

# How long until X event occurs?
bday = datetime.date(2024, 10, 20)
until_bday = bday - tday  # until_bday is a timedelta
print(until_bday)  # prints days, min, sec, micro
print(until_bday.days)  # prints only days
print(until_bday.total_seconds())  # prints only secs

# datetime.time (hours, min, sec, microsecs)
# naive by default
# tzinfo makes aware
t = datetime.time(12, 30, 15, 100000)
print(t)
print(t.hour)

# datetime.date = date functionality
# datetime.time = time functionality

# datetime.datetime = both
dt = datetime.datetime(2023, 10, 18, 12, 30, 15, 100000)
print(dt)
print(dt.date())
print(dt.time())
print(dt.year)
# 7 days from now
tdelta = datetime.timedelta(days=7)
print(dt + tdelta)
# 12 hours from now
tdelta = datetime.timedelta(hours=12)
print(dt + tdelta)
