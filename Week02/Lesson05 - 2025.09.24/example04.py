student = {"name": "John", "age": 50, "department": "IT"}

print(student, type(student))
# {'name': 'John', 'age': 50, 'department': 'IT'} <class 'dict'>

print(student["name"])  # John

print(student.get("age"))  # 50

# print(student["surname"])  # KeyError: 'surname'
print(student.get("surname"))  # None


