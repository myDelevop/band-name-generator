import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
week = now.weekday()

if year == 2020:
    print("Wear a facemask")
if month == 1:
    print("January")

print(week)

date_of_birth = dt.datetime(year=1993, month=12, day=29)
print(date_of_birth)