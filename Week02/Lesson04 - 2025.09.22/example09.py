"""
SETS

Sets (unordered, unchangeable, and unindexed)
Sets are contain multiple items like strings, numbers, boolean values, other lists, other tuples, etc.

set = {item1, item2, item3}
set = set(item1, item2, item3)
"""

students = {"Jack", "Jim", "John", "Jill", "Jerry"}
print(students, type(students))
# {'John', 'Jack', 'Jill', 'Jim', 'Jerry'} <class 'set'>

print(len(students))  # 5

students.pop()
print(students)

for student in students:
    print(student)

print("John" in students)  # False
