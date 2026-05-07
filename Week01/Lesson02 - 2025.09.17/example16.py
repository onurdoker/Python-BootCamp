import random

# randint function generates a random integer between the given two numbers
random_number = random.randint(1, 10)
# print(random_number)

# Game

guess = int(input("Please the number you guessed: "))
if guess == random_number:
    print(
        f"Congratulations! \nYou correctly guessed the number\n{guess} is the correct number"
    )
else:
    print("You did not guess the number \nTry again")
    print(f"Randomly selected number is {random_number}")
