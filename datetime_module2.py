import datetime
import pytz

# alternative constructors
dt_today = datetime.datetime.today() #tz = 0
dt_now = datetime.datetime.now() #tz = input
dt_utcnow = datetime.datetime.utcnow() #tz = input
# \/\/\/ same output (minus execution time)
print(dt_today)
print(dt_now)
print(dt_utcnow)

# time zones (use pytz)
# pip install pytz
# make time zone aware datetime
dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)
print()  # for readability in this tutorial
######################################
# Pass in your time zone
dt_central = dt_utcnow.astimezone(pytz.timezone('US/Central'))
print(dt_central)
print() # for readability in this tutorial
######################################
# make your local time zone aware
dt_central = datetime.datetime.now()
central_tz = pytz.timezone('US/Central')
dt_central = central_tz.localize(dt_central)
print(dt_central)
print() # for readability in this tutorial
# since local tz is now aware, we can use it to calculate other tz's
dt_east = dt_central.astimezone(pytz.timezone('US/Eastern'))
print(f"Eastern time is:  {dt_east}")
print() # for readability in this tutorial

# print in a specific format
# print(dt_central.strftime('args (from documentation'))
# common args from doc
print(dt_central.strftime('%B %d, %Y'))
print() # for readability in this tutorial

# convert string to datetime
dt_str = "October 18, 2023"
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)
print() # for readability in this tutorial

# strftime - Datetime to String
# strptime - String to Datetime