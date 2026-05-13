"""
FUNCTIONS

Naming and organizing repetitive tasks into code blocks, known as functions, which can be easily called when needed

Functions have 4 kinds:
- without parameters and not return value
- without parameters and with return value
- with parameters and not return value
- with parameters and with return value
"""

number = 5
print(number * number)

number = 8
print(number * number)

number = 10
print(number * number)


# using a function to make the code more clean and reusable
def calculate_square(number):
    return number * number


print(calculate_square(5))
print(calculate_square(8))
print(calculate_square(10))
