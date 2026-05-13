"""
This script demonstrates the random module for generating random numbers and shuffling lists.
"""

import random

# * random float number between 0 and 1
print("Random a number between 0 - 1: ", random.random())
# Random a number between 0 - 1:  0.7789221838418057

# * random integer number between 1 and 100
print("Random a number between 0 - 100: ", random.randint(1, 100))
# Random a number between 0 - 100:  87

# * random float number between 1 and 5
print("Random a float number between 1 - 5: ", random.uniform(1, 5))
# Random a float number between 1 - 5:  1.3752715215799616

# * random choice from a list
colors = ["red", "yellow", "pink"]
chosen_color = random.choice(colors)
print("Chosen color: ", chosen_color)

# * random shuffle of a list
random.shuffle(colors)
print("Shuffled colors: ", colors)
