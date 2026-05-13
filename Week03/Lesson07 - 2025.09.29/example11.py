"""
Demonstrates age validation with multiple conditions and exception handling.
"""

print("===== AGE CONTROL =====")

try:
    age = int(input("Enter your age: "))

    if age < 0:
        raise ValueError("Age cannot be less than 0")

    elif age < 18:
        raise ValueError("Age cannot be less than 18")

    elif age > 120:
        raise ValueError("Age cannot be greater than 120")

    print("Progress continue...")

except ValueError as error:
    print(f"Number errors:  {error}")
except Exception as error:
    print(f"Other errors:  {error}")

print("Control finished")
