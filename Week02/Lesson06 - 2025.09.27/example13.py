"""
Use default values in variable declarations and function parameters
"""


def calculate_square(radius=1, pi=3.14):
    return pi * radius**2


# print(calculate_square())  #
print(calculate_square(5))  # 78.5
print(calculate_square(5, 3.14159))  # 78.53975
