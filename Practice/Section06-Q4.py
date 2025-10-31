"""
Write a program that calculates area using the sine theorem
"""

import math


def calculate_area(a, b, theta):

    theta_rad = math.radians(theta)

    area = a * b / (2 * math.sin(theta_rad))

    return area


a = float(input("Please enter the length of side a: "))
b = float(input("Please enter the length of side b: "))
theta = float(input("Please enter the angle of rotation (in degrees): "))

area = calculate_area(a, b, theta)
print(f"The area of the triangle is {area:.2f} square units.")
