"""
Calculates the age in days since the last birthday and the days remaining until the next birthday
"""

from datetime import datetime

birthday = input("Enter your birthday (dd/mm/yyyy): ")
day, month, year = map(int, birthday.split("/"))
print(day, month, year)

bd_date = datetime(year, month, day)
print(bd_date)

today = datetime.now()
print("today", today)

this_year_bd = bd_date.replace(year=today.year)
print("this year birth day: ", this_year_bd)

if this_year_bd < today:
    print(f"{(today - this_year_bd).days} days have passed since your birthday ")

    this_year_bd = this_year_bd.replace(year=today.year + 1)

print(f"There are {(this_year_bd - today).days} days left until your birthday")
