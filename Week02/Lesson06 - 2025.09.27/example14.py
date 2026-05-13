"""
Arguments (positional arguments)
"""


def calculate_addition(*args):
    print(args, type(args))
    sum = 0
    for arg in args:
        sum += arg
    print("Calculation result: ", sum)
    return sum


calculate_addition(5, 10, 15)
# (5, 10, 15) <class 'tuple'>
# Calculation result:  30

calculate_addition(5, 10, 15, 20, 25, 30, 35, 40, 45, 50)
# (5, 10, 15, 20, 25, 30, 35, 40, 45, 50) <class 'tuple'>
# Calculation result:  275
