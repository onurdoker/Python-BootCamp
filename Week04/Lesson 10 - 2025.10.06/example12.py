"""
2. Class methods
- These are methods that belong to an object (instance) created from a class, not to an instance.
- It takes cls as its first parameter (representing the class)

- Defined using the @classmethod decorator
"""


class Student:
    school_name = "TechIstanbul Academy"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod  # Entered the method as a class method
    def school_info(cls):  # cls is used to refer to the class itself
        print(f"This students go to {cls.school_name} ")

    def student_school_info(self):
        print(f"This student's school is {self.school_name}")


Student.school_info()  # This students go to TechIstanbul Academy

student1 = Student("Jack", 20)
student1.school_info()  # This students go to TechIstanbul Academy

student1.school_name = "Ecodation"
student1.school_info()  # This students go to TechIstanbul Academy

student1.student_school_info()  # This student's school is Ecodation
