"""
Uses map and lambda to calculate squares of numbers from 1 to 10.
"""

calculate_square = list(map(lambda x: x**2, range(1, 11)))
print(calculate_square)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
