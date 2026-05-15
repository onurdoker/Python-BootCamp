"""
Take user's name, age, and hobbies, save them both in a TXT and JSON format
"""

import json

print("=== Personal Information ===")
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
hobbies = input("Please enter your hobbies (write with comma): ").split(",")

person = {"Name": name, "Age": age, "Hobbies": hobbies}

# Save to TXT file
with open("information.txt", "w", encoding="UTF-8") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")
    file.write(f"Hobbies: {','.join(hobbies)}\n")

# Save to JSON file
with open("information.json", "w", encoding="UTF-8") as file:
    json.dump(person, file, indent=4)
