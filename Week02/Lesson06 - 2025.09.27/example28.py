"""
This file demonstrates two methods to find the maximum number in a list:
an iterative approach using loops and a recursive approach.
"""


def find_max(*args):
    if len(args) == 0:
        return None
    else:
        max_number = args[0]
        for arg in args:
            if arg > max_number:
                max_number = arg
    return max_number


print(find_max(1, 3, 5, 2, 6, 4, 6, 9, 4))


def find_max2(*args):
    if len(args) == 0:
        return None
    elif len(args) == 1:
        return args[0]
    max_number = find_max2(*args[1:])
    return args[0] if args[0] > max_number else max_number


print(find_max2(1, 3, 5, 2, 6, 4, 6, 9, 4))
