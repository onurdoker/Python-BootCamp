"""
Methods

Functions defined within a class
The self parameter is mandatory (automatically passed)

Self Keyword
Every method takes self as its first parameter
in Python, self is automatically passed when calling object,method().
You can use a different name instead of self, but it is not considered best practices
"""


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show_info(self):
        return f"{self.brand}, {self.model}"


car1 = Car("Toyota", "Corolla")
print(car1.brand)  # Toyota

print(car1.show_info())  # Toyota, Corolla
