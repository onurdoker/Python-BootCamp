"""
Methods in OOP

|===================|===========|=======================|===============================|===============================================|
|   Type            | Parameter |    Accessible         |    Call Location              |    Purpose                                    |
|===================|===========|=======================|===============================|===============================================|
| Instance method   | self      | Instance variables    | Using the object              | Methods define object-specific operations     |
| Class method      | cls       | Class variables       | Via the class or the object   | Operations related to all classes             |
| Static method     |           | None of them          | Via the class or the object   | Helper functions                              |
|===================|===========|=======================|===============================|===============================================|

"""

"""
1. Normal (Instance) Methods
- These are methods that belong to an object (instance) created from a class
- The first parameter must be self, which represents the object itself
"""


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


student1 = Student("Jack", 20)
student1.show_info()  # Name: Jack, Age: 20
