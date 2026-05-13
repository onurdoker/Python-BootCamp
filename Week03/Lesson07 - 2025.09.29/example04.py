"""
Demonstrates raising and catching ValueError for invalid input validation.
"""

try:
    age = int(input("Please enter your age: "))
    if age < 0 or age > 150:
        raise ValueError("age must be between 0 and 150")
except ValueError as error:
    print("Error: ", error)

print("Program ended")
