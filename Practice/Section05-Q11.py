"""
Write a code to find and print all prime numbers from 2 and 1000
"""


def is_royal():

    for number in range(2, 1001):

        if number > 1:
            for i in range(2, int(number / 2) + 1):
                if number % i == 0:
                    break
            else:
                print(number)


print(is_royal())
