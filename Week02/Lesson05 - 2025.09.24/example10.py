week_in = {"Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5}
week_end = {"Saturday": 6, "Sunday": 7}

week_days = {}

week_days.update(week_in)
week_days.update(week_end)
print(week_days)

print(len(week_in))

day = "Sunday"

if day in week_days:
    print("day added")
