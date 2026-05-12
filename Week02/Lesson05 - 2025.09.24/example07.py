"""
Student ID System
"""

# First answer
students = []

print("=" * 5, "Student Score System", "=" * 5)
print("To exit press Q")

while True:
    name = input("Please enter student's name: ")
    if name.lower() == "q":
        break
    else:
        score = int(input("Please enter student's score: "))
        students.append({"name": name, "score": score})

print(students)

# Second answer
students = []

while True:
    name = input("Please enter student's name: ")
    if name.lower() == "quit":
        break

    surname = input("Please enter student's surname: ")
    if surname.lower() == "quit":
        break

    score = float(input("Please enter student's score: "))
    if (score < 0.0) | (score > 100.0):
        break

    students.append({"name": name, "surname": surname, "score": score})

print(students)
