day = int(input("Which day of week is it? "))

if day == 1 or day == 3 or day == 6:
    print("Python Bootcamp is on this day!")
elif day == 2 or day == 4 or day == 5 or day == 7:
    print("Python Bootcamp is not on this day!")
else:
    print("Invalid input, please enter a number between 1 and 7.")
