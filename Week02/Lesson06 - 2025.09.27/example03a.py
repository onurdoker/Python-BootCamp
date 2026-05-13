"""
FUNCTIONS

with parameters and not return value
"""


def sum_of_two_numbers(number1, number2):
    calculate = number1 + number2
    print(f"{number1} + {number2} = {calculate}")


sum_of_two_numbers(5, 8)  # 5 + 8 = 13
sum_of_two_numbers(10, 20)  # 10 + 20 = 30

x = sum_of_two_numbers(7, 8)
print(x, type(x))  # None <class 'NoneType'>
