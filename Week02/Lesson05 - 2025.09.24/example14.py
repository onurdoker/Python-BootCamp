school = {
    "9A": [
        {"name": "John", "number": "101"},
        {"name": "Jack", "number": "102"},
    ],
    "10B": [
        {"name": "Jim", "number": "201"},
        {"name": "Jill", "number": "202"},
    ],
}

for class_, students in school.items():
    print(f"\n{class_}")
    for student in students:
        print(f" - {student['name']} (Number: {student['number']})")
