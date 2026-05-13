"""
Debugging, identification, and correction of errors in code are crucial for ensuring the reliability and functionality of software applications.
"""

# Without debugging, the code may produce unexpected results or errors.
age = int(input("Please enter your age: "))
print("Your age is:", age)
if age < 18:
    print("You are not of legal age")
else:
    print("You are of legal age")


# with debugging, the code will produce expected results and errors or errors
try:
    age = int(input("Please enter your age: "))
    print("Your age is: ", age)
    if age < 18:
        print("You are not of legal age")
    else:
        print("You are of legal age")
except ValueError:  # Handle any exceptions that may occur during execution
    print("Invalid input. Please enter a valid integer for age.")

print("Program ended")
