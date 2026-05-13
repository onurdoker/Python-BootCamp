"""
When predict a possible error, we can intentionally cause the error ourselves by using raise
"""

age = int(input("Please enter your age: "))
if age < 0 or age > 150:
    raise ValueError("age must be between 0 and 150")
else:
    print("Your age is:", age)
    print("You are of legal age")
