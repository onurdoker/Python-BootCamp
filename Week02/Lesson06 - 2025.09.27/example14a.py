"""
Arguments (positional arguments)
"""


def calculate_addition(x, *args):
    print(args, type(args))
    sum = 0
    for arg in args:
        sum += arg * x
    print("Calculation result: ", sum)
    return sum


calculate_addition(2, 5, 10, 15)
# (5, 10, 15) <class 'tuple'>
# Calculation result:  60

calculate_addition(1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50)
# (5, 10, 15, 20, 25, 30, 35, 40, 45, 50) <class 'tuple'>
# Calculation result:  275
