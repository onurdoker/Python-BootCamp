"""
Take two numbers and a mathematical operation from the user and perform the calculation.
"""


def calculate_addition(number1, number2):
    return number1 + number2


def calculate_subtraction(number1, number2):
    return number1 - number2


def calculate_multiplication(number1, number2):
    return number1 * number2


def calculate_division(number1, number2):
    return number1 / number2


def calculation(number1, number2, process):
    if process == "+":
        return calculate_addition(number1, number2)
    elif process == "-":
        return calculate_subtraction(number1, number2)
    elif process == "*":
        return calculate_multiplication(number1, number2)
    elif process == "/":
        return calculate_division(number1, number2)
    else:
        return "Invalid process"


def main():
    process = input("Please enter your process (+,-,*,/ only): ")
    number1 = float(input("Please enter your first number: "))
    number2 = float(input("Please enter your second number: "))
    answer = calculation(number1, number2, process)
    print(f"{number1} {process} {number2} = {answer}")


main()
