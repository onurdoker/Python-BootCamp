"""
This program calculates circle properties (area, circumference), power operations, and trigonometric functions based on user input for radius and angle.
import math
"""

import math

try:
    radius = float(input("Enter the radius of the circle: "))
    if radius <= 0:
        raise ValueError("Radius must be greater than 0")

    # Calculation with math library
    circle_area = math.pi * math.pow(radius, 2)
    circle_circumference = 2 * math.pi * radius
    print("\nCircle knowledge:")
    print(f"Circle radius: {radius}")
    print(f"Circle circumference: {circle_circumference:.3f}")
    print(f"Circle area: {circle_area:.2f}")

    # Square and power functions
    print("\nSquare root and power of the radius:")
    sqrt_ = math.sqrt(radius)
    power_ = math.pow(radius, 2)
    cube = math.pow(radius, 3)
    print(f"Square root of the radius: {sqrt_:.2f}")
    print(f"Power of the radius: {power_:.2f}")
    print(f"Cube of the radius: {cube:.2f}")

    # Trigonometric functions
    print("\nTrigonometric functions: ")
    angle = float(input("Enter the angle (degree): "))
    angle_rad = math.radians(angle)
    print(f"Sine of the angle: {math.sin(angle_rad):.2f}")
    print(f"Cosine of the angle: {math.cos(angle_rad):.2f}")
    print(f"Tangent of the angle: {math.tan(angle_rad):.2f}")

except ValueError as error:
    print(f"Error: {error}")
except Exception as error:
    print(f"An unexpected error occurred: {error}")

print("Calculations ended")
