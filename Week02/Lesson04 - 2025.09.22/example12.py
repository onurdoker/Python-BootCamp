"""
Number guessing game
"""

import random

random_number = random.randint(1, 10)
your_answers = []
while True:
    guess = int(input("Please enter your guess (1 to 10): "))
    if guess <= 0 or guess >= 11:
        print("You have to enter a number between 1 and 10")
        pass
    elif guess == random_number:
        print("Congratulations! You find correct number")
        break
    elif guess < random_number:
        print("Your guess is too low, try again")
        your_answers.append(guess)
    else:
        print("Your guess is too high, try again")
        your_answers.append(guess)
print(f"Your answers: {your_answers}")
