"""
This is a number guessing game where the computer generates a random number (1-100) and the player has 10 attempts to guess it, with game results saved to a file.
"""

import random

with open("game.txt", "w") as file:
    while True:
        answer = int(
            input("Choose your: \n1 for Game \n2 for Statistics \n3 for Exit \n")
        )
        if answer == 1:
            file = open("game.txt", "a")
            random_number = random.randrange(1, 100)
            file.write(str(random_number) + ", ")
            guess_number = 10
            ceil = 0
            top = 100
            while guess_number >= 1:
                guess = int(input(f"Enter a number {ceil} - {top} "))
                file.write(str(guess) + ", ")
                if guess == random_number:
                    file.write(f"{random_number} +  you win")
                    print("Congratz")
                    break
                elif guess > random_number:
                    print("Enter lower number")
                    top = guess
                elif guess < random_number:
                    print("Enter higher number")
                    ceil = guess
                guess_number -= 1
                print(f"You have {guess_number} guesses left")
                if guess_number == 0:
                    file.write(f"{random_number} +  you lose")
                    print("You lose")
                    break

        elif answer == 2:
            with open("game.txt", "r") as file:
                print(file.read())
        elif answer == 3:
            print("Exiting the program")
            break
