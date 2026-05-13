"""
Demonstrates finally block for cleanup operations regardless of exceptions.
"""

print("===== SOURCE MANAGEMENT =====")

connection_open = True

try:
    name = input("Enter your name: ")

    age = int(input("Enter your age: "))

    print(f"Hello {name}, you are {age} years old")
except ValueError:
    print("Error: Please enter a valid age")

finally:
    if connection_open:
        print("Connection closed")
    print("Finally block executed")

print("Program finished successfully")
