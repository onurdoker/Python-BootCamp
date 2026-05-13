"""
The try-except-finally block ensures that user feedback is provided after each attempt,
and a final success message is displayed when valid inputs are entered
"""

print("====== USER REGISTRATION SYSTEM ======")
while True:
    try:
        name = input("Enter your name: ")
        if len(name) < 2:
            raise ValueError("Name cannot be less than 2 characters")
        age = int(input("Enter your age: "))
        if age < 0 or age > 150:
            raise ValueError("Age must be between 0 and 150")

    except ValueError as error:
        print("Error: " + str(error))
    else:
        print("Welcome " + name)
        break
    finally:
        print("-------")

print("Program finished successfully")
