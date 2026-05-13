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
    if not (process == "+" or process == "-" or process == "*" or process == "/"):
        return print("Invalid process input")

    def get_number():
        return float(input("Please enter your number: "))

    number1 = get_number()
    number2 = get_number()

    answer = calculation(number1, number2, process)
    print(f"{number1} {process} {number2} = {answer}")
    return main()


if __name__ == "__main__":
    print("Welcome to Calculator Program!")
    main()
