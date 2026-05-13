"""
Calculate Average
"""


def calculate_average(*args):
    total = 0
    for arg in args:
        total += arg
    return total / len(args) if args else 0


print(calculate_average(3, 5, 7, 9))
print(calculate_average(3, 5))
