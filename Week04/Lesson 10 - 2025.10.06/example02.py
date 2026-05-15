"""
Class

Class definition: It is a blueprint for objects, specifying what attributes and functions (methods) the objects can have
"""


class Student:
    def __init__(self, name, age, average_score):
        self.name = name
        self.age = age
        self.average_score = average_score

    def student_info(self):
        return (
            f"{self.name}, {self.age} years old, average score is {self.average_score}"
        )

    def update_student_info(self, **kwargs):
        for key, value in kwargs.items():
            if key in self.__dict__:
                self.__dict__[key] = value
        return self


# Usage
student1 = Student("John", 48, 3.5)
print(student1.student_info())
# John, 48 years old, average score is 3.5

student2 = Student("Jill", 22, 2.7)
print(student2.student_info())
# Jill, 22 years old, average score is 2.7

student1.update_student_info(name="Jack")
print(student1.student_info())
# Jack, 48 years old, average score is 3.5
