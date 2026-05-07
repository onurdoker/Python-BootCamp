"""
Fizz - Buzz Game

"""

last_number = int(input('Please enter the last number" '))

for dd in range(1, last_number + 1):
    if (dd % 3 == 0) and (dd % 5 == 0):
        print(dd, "FizzBuzz")
    elif dd % 3 == 0:
        print(dd, "Fizz")
    elif dd % 5 == 0:
        print(dd, "Buzz")
    else:
        print(dd)
