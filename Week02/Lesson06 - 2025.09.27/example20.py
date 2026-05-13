"""
Sorting a list
"""

students = [("John", 39), ("Jack", 20), ("Jim", 47), ("Jerry", 32)]

sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print(sorted_students)
# [('Jim', 47), ('John', 39), ('Jerry', 32), ('Jack', 20)]
