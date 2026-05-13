"""
Generates a random password of a specified length using letters, digits, and special characters.
"""

import random
import string


def password_generator(length):
    character = string.ascii_letters + string.digits + "!@#$%"
    return "".join(random.choice(character) for _ in range(length))


try:
    length_ = int(input("Enter the length of the password: "))
    print("Your password: ", password_generator(length_))
except:
    print("Please enter a valid number")
