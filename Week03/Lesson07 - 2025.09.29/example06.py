"""
The code uses a try block to attempt the division operation.
it catches specific exceptions (ZeroDivisionError and ValueError) and prints appropriate error messages.
finally block is used to display a final success message.
"""

print("===== DIVISION OPERATION =====")
try:
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))

    answer = number1 / number2

    print(f"Answer is: {number1} / {number2} = {answer}")

except ZeroDivisionError:
    print("Error: cannot divide by zero")

except ValueError:
    print("Error: invalid value entered")

print("Program finished successfully")
