"""
JSON Files
"""

import json

students = [
    {"name": "Jack", "age": 22, "department": "Computer Engineering"},
    {"name": "Jill", "age": 40, "department": "Chemical Engineering"},
    {"name": "John", "age": 35, "department": "Mechanical Engineering"},
    {"name": "Jill", "age": 28, "department": "Physics Engineering"},
]

with open("students.json", "w", encoding="UTF=8") as file:
    json.dump(students, file, indent=4)

with open("students.json", "r") as file:
    data = json.load(file)
    print(data, type(data))
    for student in data:
        print(student["age"], type(student["age"]))
