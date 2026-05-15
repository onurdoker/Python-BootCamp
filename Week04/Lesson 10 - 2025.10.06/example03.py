"""
Common usage
"""


class Car:
    pass


car1 = Car()
car2 = Car()


class Student:
    pass


student1 = Student()
student1.name = "Jack"
print(student1, type(student1), student1.name)
# <__main__.Student object at 0x10344f0e0> <class '__main__.Student'> Jack

# print(student1.surname)
# AttributeError: 'Student' object has no attribute 'surname'

student2 = Student()
print(type(student2))
# <class '__main__.Student'>

student2.name = "Jill"
student2.surname = "Doe"
print(student2.name, student2.surname)
# Jill Doe
