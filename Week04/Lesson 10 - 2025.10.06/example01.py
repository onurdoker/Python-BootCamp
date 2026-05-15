"""
OOP - Object-Oriented Programming

Difference from structured programming: Code reusability, modularity and ease of maintenance.
Real-world analogy: objects -> attributes + behaviors (methods)
In Python, everything is an object - even types like int, str, and list are objects
"""

# Functional approach before OOP


def create_student(name, age, average_score):
    return {"name": name, "age": age, "average_score": average_score}


def student_info(student):
    return f"{student['name']}, {student['age']}  years old, average score is {student['average_score']}"


def student_info_update(student, **kwarg):
    for key, value in kwarg.items():
        if key in student:
            student[key] = value
    return student


# Usage
student = create_student("John", 48, 3.5)
print(student_info(student))
# John, 48  years old, average score is 3.5

student_info_update(student, name="Jane")
print(student)
# {"name": "Jane", "age": 48, "average_score": 3.5}
