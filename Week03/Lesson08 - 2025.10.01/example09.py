"""
Simulates rolling three dice and checks if all three dice show the same number. The game continues until a win condition is met.
"""

import random

try_number = 0
symbols = [1, 2, 3, 4, 5, 6, 7]

while True:
    input("Press enter to roll the dice ")
    while True:
        result = [str(random.choice(symbols)) for _ in range(3)]
        print(" | ".join(result))
        try_number += 1

        if result[0] == result[1] == result[2]:
            print("You win!")
            print("Try Number: ", try_number)
            break
        else:
            print("You lose!")
