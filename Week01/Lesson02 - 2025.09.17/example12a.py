"""
Match - Case statement in Python
"""

day = int(input("Which day of week is it? "))

match day:
    case 1 | 3 | 6:
        print("Python Bootcamp is on this day!")
    case 2 | 4 | 5 | 7:
        print("Python Bootcamp is not on this day!")
    case _:
        print("Invalid input, please enter a number between 1 and 7.")
