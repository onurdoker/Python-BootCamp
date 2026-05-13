"""
Calculate circle area
"""


def calculate_circle_area(radius):
    pi = 3.14
    return pi * radius**2


radius = float(input("Please enter your radius: "))
print(
    f"The area of a circle a radius of {radius} units is {calculate_circle_area(radius)} square units."
)
