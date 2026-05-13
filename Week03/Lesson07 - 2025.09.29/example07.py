"""
This example validates user age input using try-except blocks and raises ValueError for invalid ages.
"""

print("===== CALCULATION BIRTH YEAR ======")
while True:
    try:
        age = int(input("Enter your age: "))

        if age < 0:
            raise ValueError("Age cannot be less than 0")

        birth_year = 2025 - age

        print(f"Birth Year: {birth_year}")
        break

    except ValueError:
        print("Error: Value entered is not an integer (For example: 25)")

        continue_ = input("To continue press Y, to exit press N: ")
        if continue_.upper() == "N":
            print("Program finished")
            break

print("Thanks for using our program")
