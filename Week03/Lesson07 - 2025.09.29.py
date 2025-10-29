# ! First Example
# age = int(input("Enter your age: "))
# print("Age: ", age)
# if age < 18:
#     print("Not enough adults")
# else:
#     print("Enjoy!")

# ! Second Example
# try:
#     age = int(input("Enter your age: "))
#     print("Age: ", age)
#     if age < 18:
#         print("Not enough adults")
#     else:
#         print("Enjoy!")
# except:
#     pass

# ! Third Example
# try:
#     age = int(input("Enter your age: "))
#     print("Age: ", age)
#     if age < 18:
#         print("Not enough adults")
#     else:
#         print("Enjoy!")
# except ValueError:
#     print("Please enter a valid integer for age.")

# ! Fourth Example
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

# friends = ["Ali", "Veli", "Onur"]
# print(friends[4])  # => Index Error

# ! Fifth Example
# * If we can predict the possible errors that might occur, we can take precautions
# try:
#     number = int(input("Enter a number: "))
#     answer = 100 / number
# except ValueError:
#     print("Value entered is not an integer")
# except ZeroDivisionError:
#     print("Division by zero encountered")
# except Exception as error:
#     print("An error occurred: {}".format(error))

# ! Sixth Example
# * When predict a possible error, we can intentionally cause the error ourselves by using raise
# age = int(input("Enter your age: "))
# if age < 0 or age > 150:
#     raise ValueError("age must be between 0 and 150")
# else:
#     print("Your age is:", age)
#     print("Valid age")

# ! Seventh Example
# try:
#     age = int(input("Enter your age: "))
#     if age < 0 or age > 150:
#         raise ValueError("Age must be between 0 and 150.")
#     else:
#         print("Your age is: ", age)
# except ValueError as error:
#     print("Value entered is not an integer")

# ! Eighth Example
"""
The try-except-finally block ensures that user feedback is provided after each attempt,
and a final success message is displayed when valid inputs are entered
"""
# print("====== USER REGISTRATION SYSTEM ======")
# while True:
#     try:
#         name = input("Enter your name: ")
#         if len(name) < 2:
#             raise ValueError("Name cannot be less than 2 characters")
#         age = int(input("Enter your age: "))
#         if age < 0 or age > 150:
#             raise ValueError("Age must be between 0 and 150")

#     except ValueError as error:
#         print("Error: " + str(error))
#     else:
#         print("Welcome " + name)
#         break
#     finally:
#         print("-------")

# print("Program finished successfully")

# ! Nineth Example
"""
The code uses a try block to attempt the division operation.
it catches specific exceptions (ZeroDivisionError and ValueError) and prints appropriate error messages.
finally block is used to display a final success message.
"""
# print("===== DIVISION OPERATION =====")
# try:
#     number1 = float(input("Enter first number: "))
#     number2 = float(input("Enter second number: "))

#     answer = number1 / number2

#     print(f"Answer is: {number1} / {number2} = {answer}")

# except ZeroDivisionError:
#     print("Error: cannot divide by zero")

# except ValueError:
#     print("Error: invalid value entered")

# print("Program finished successfully")

# ! Tenth Example
# print("===== CALCULATION BIRTH YEAR ======")
# while True:
#     try:
#         age = int(input("Enter your age: "))

#         if age < 0:
#             raise ValueError("Age cannot be less than 0")

#         birth_year = 2025 - age

#         print(f"Birth Year: {birth_year}")
#         break

#     except ValueError:
#         print("Error: Value entered is not an integer (For example: 25)")

#         continue_ = input("To continue press Y, to exit press N: ")
#         if continue_.upper() == "N":
#             print("Program finished")
#             break

# print("Thanks for using our program")

# ! Eleventh Example
# print("===== FRUIT LIST =====")
# fruits = ["Apple", "Pear", "Strawberry", "Banana", "Orange"]
# print(f"Fruits: {fruits}")

# try:
#     index = int(input("Enter which fruit you want (0-4): "))

#     selected_fruit = fruits[index]

#     print(f"Selected fruit: {selected_fruit}")

# except ValueError:
#     print("Error: Value entered is not an integer (For example: 1)")

# except IndexError:
#     print(f"Error: Index out of range (0-4)")

# else:
#     print("Bon appétit")

# finally:
#     print("Program finished successfully")

# ! Twelfth Example
# print("===== MULTIPLE ERROR HANDLING =====")
# numbers = [10, 20, 30, 40, 50]
# print(f"Numbers: {numbers}")

# try:
#     index = int(input("Which number you want to select (0-4): "))

#     divider = int(input("What number woul you like to divide this by? "))

#     selected_number = numbers[index]

#     answer = selected_number / divider

#     print(f"Answer is: {selected_number} / {divider} = {answer}")

# except (ValueError, ZeroDivisionError, IndexError) as error:
#     print(f"Error: {type(error).__name__}")

#     if isinstance(error, ValueError):
#         print("Please enter a valid integer")
#     elif isinstance(error, ZeroDivisionError):
#         print("You cannot divide by zero")
#     elif isinstance(error, IndexError):
#         print("Index out of range")

# print("Program continue...")

# ! Thirteenth Example
# print("===== SOURCE MANAGEMENT =====")

# connection_open = True

# try:
#     name = input("Enter your name: ")

#     age = int(input("Enter your age: "))

#     print(f"Hello {name}, you are {age} years old")
# except ValueError:
#     print("Error: Please enter a valid age")

# finally:
#     if connection_open:
#         print("Connection closed")
#     print("Finally block executed")

# print("Program finished successfully")

# ! Fourteenth Example
# print("===== AGE CONTROL =====")

# try:
#     age = int(input("Enter your age: "))

#     if age < 0:
#         raise ValueError("Age cannot be less than 0")

#     elif age < 18:
#         raise ValueError("Age cannot be less than 18")

#     elif age > 120:
#         raise ValueError("Age cannot be greater than 120")

#     print("Progress continue...")

# except ValueError as error:
#     print(f"Number errors:  {error}")
# except Exception as error:
#     print(f"Other errors:  {error}")

# print("Control finished")
