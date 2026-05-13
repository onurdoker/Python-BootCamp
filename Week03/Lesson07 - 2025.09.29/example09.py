"""
Demonstrates multiple exception handling for ValueError, ZeroDivisionError, and IndexError.
"""

print("===== MULTIPLE ERROR HANDLING =====")
numbers = [10, 20, 30, 40, 50]
print(f"Numbers: {numbers}")

try:
    index = int(input("Which number you want to select (0-4): "))

    divider = int(input("What number would you like to divide this by? "))

    selected_number = numbers[index]

    answer = selected_number / divider

    print(f"Answer is: {selected_number} / {divider} = {answer}")

except (ValueError, ZeroDivisionError, IndexError) as error:
    print(f"Error: {type(error).__name__}")

    if isinstance(error, ValueError):
        print("Please enter a valid integer")
    elif isinstance(error, ZeroDivisionError):
        print("You cannot divide by zero")
    elif isinstance(error, IndexError):
        print("Index out of range")

print("Program continue...")
