"""
Value Error         => invalid value entered like int('abc')
Index Error         => enter missing values like entering 5 value in list[10]
Type Error          => invalid type entered like str('abc')
Key Error           => not entered key value in dictionary
ZeroDivisionError   => division by zero like 5 / 0
AttributeError      => Attempting to access non-existent attribute or method of an object
Exception           => When an error or exception condition occurs that disrupts the normal flow of a program
NameError           => When accessing an undefined variable
"""

#  ValueError
try:
    number = int(input("Please enter a number: "))
    answer = 100 / number
except ValueError:
    print("Invalid enter, please enter a valid integer.")

#  ZeroDivisionError
try:
    number = int(input("Please enter a number: "))
    answer = 100 / number
except ZeroDivisionError:
    print("Cannot divide by zero. Please enter a non-zero number.")

# Exception
try:
    number = int(input("Please enter a number: "))
    answer = 100 / number
except Exception as error:
    print("An error occurred: ", str(error))
