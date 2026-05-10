"""
Lists => Ordered, changeable and allow duplicate values.

* Lists are contain multiple items like strings, numbers, boolean values, other lists, etc.
"""

student_name = "John"
student_surname = "Doe"
student_number = 123
student_attend = True
student_average_score = 3.60

student1 = [
    student_name,
    student_surname,
    student_number,
    student_attend,
    student_average_score,
]

print(student1, type(student1))
# ['John', 'Doe', 123, True, 3.6] <class 'list'>

student2 = ["Jack", "Black", 14, True, 3.2]
print(student2, type(student2))
# ['Jack', 'Black', 14, True, 3.2] <class 'list'>


# * Lists are indexed.
print(len(student1))  # 5
print(student1[4])  # 3.60

print("mary" in student1)  # False
print("Jack" in student2)  # True

for student_knowledge in student1:
    print(student_knowledge)

for dd in range(len(student1)):
    print(student1[dd])
