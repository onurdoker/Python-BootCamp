"""
This script demonstrates common math module functions for mathematical operations including pi, power, square root, rounding, and trigonometric calculations.
"""

import math

print("Pi number: ", math.pi)  # Pi number:  3.141592653589793
print("Power of the number: ", math.pow(5, 6))  # Power of the number:  15625.0

print("Square root of the number: ", math.sqrt(16))  # Square root of the number:  4.0
print("Round the number: ", round(4.502))  # Round the number:  5

print(
    "Calculating cos an angle: ", math.cos(math.radians(90))
)  # Calculating cos an angle:  6.123233995736766e-17

print(
    "Calculating cos an angle: ", math.cos(math.radians(math.pi / 4))
)  # Calculating cos an angle:  0.9999060498015505
