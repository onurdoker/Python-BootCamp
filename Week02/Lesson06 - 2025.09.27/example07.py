"""
Power control application
"""


def control_power(power, number):
    if number % power == 0:
        return number // power


print(control_power(15, 5))  # 3
print(control_power(10, 3))  # None
