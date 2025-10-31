"""
Write a program that tries to find a randomly generated number stored by computer
"""

import random

secret_number = random.randint(1, 100)

print("Ihave thought of a number between 1 and 100. Try to guess it.")
n = 10

while True:
    if n > 0:
        guess = int(input("Please enter your guess: "))

        if guess < secret_number:
            print("Your guess is too low. Try again.")
        elif guess > secret_number:
            print("Your guess is too high. Try again.")
        else:
            print(f"Congratulations! You found my number {secret_number}!")
            break

        n -= 1
        print(f"You have {n} guess left.")
    else:
        print("Sorry, you lost the game.")
        break
print("Thank you for playing!")
