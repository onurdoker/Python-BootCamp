"""
Calculate the age from a person's birth year
"""


def calculate_age(birth_year):
    age = 2025 - birth_year
    return age


year = int(input("Please enter your birth year: "))
print(f"if you were born at {year}, you are {calculate_age(year)} years old.")
