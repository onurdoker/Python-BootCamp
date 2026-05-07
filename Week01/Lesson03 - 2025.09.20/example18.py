"""
Let's create a code where a computer generates a random number between 1 and 10, and the user tries to guess it. The program will provide guidance based on the guess (too high or too low) until the user guesses correctly.)
"""

import random

hold_number = random.randint(1, 10)

while True:
    number = int(input("Please enter a number (1 - 10): "))
    if number <= 0 or number >= 11:
        print("You have to enter a number between 1 and 10")
        continue
    elif number == hold_number:
        print("Congratulations! You find correct number")
        break
    elif number < hold_number:
        print("Too low, try again.")
    elif number > hold_number:
        print("Too high, try again.")
    else:
        print("Invalid number")
