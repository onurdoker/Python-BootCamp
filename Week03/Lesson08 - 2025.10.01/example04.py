"""
This script demonstrates the datetime module for retrieving and formatting current date and time information.
"""

import datetime  # * using for date and time operations

now_ = datetime.datetime.now()
print("Now: ", now_)  # Now:  2026-05-13 22:14:06.145755
print("Year: ", now_.year)  # Year:  2026
print("Month: ", now_.month)  # Month:  5
print("Day: ", now_.day)  # Day:  13
print("Hour: ", now_.hour)  # Hour:  22
print("Minutes: ", now_.minute)  # Minutes:  14
print("Microseconds: ", now_.microsecond)  # Microseconds:  145755

print("Date: ", now_.date())  # Date:  2026-05-13
print("Which day of week: ", now_.weekday())  # Which day of week:  2
print("Which day of week: ", now_.strftime("%A"))  # Which day of week:  Wednesday
print("Which mount: ", now_.strftime("%B"))  # Which mount:  May
print("Which day of mount: ", now_.strftime("%d"))  # Which day of mount:  13
print("Format of time: ", now_.strftime("%d/%m/%Y"))  # Format of time:  13/05/2026
print("Hour format: ", now_.strftime("%H:%M:%S"))  # Hour format:  22:14:06

# to change the day name or month name, you can use strftime method
print(
    "Week Day: ", now_.strftime("%A").replace("Wednesday", "Carsamba")
)  # Week Day:  Carsamba
print("Month: ", now_.strftime("%B").replace("October", "Kasim"))
