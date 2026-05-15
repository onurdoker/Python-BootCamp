"""
__init__ => constructor method
It is automatically called when an object is created.
Defines the initial state (attributes)

self => instance
"""


class Car:
    wheel_number = 4

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


car1 = Car("Volkswagen", "Golf")
print("Car1's wheel number: ", car1.wheel_number)  # Car1's wheel number:  4
print(
    "Car1's brand and model: ", car1.brand, car1.model
)  # Car1's brand and model:  Volkswagen Golf

car2 = Car("Renault", "Megane 3")
print("Car2's wheel number: ", car2.wheel_number)  # Car2's wheel number:  4
print(
    "Car2's brand and model: ", car2.brand, car2.model
)  # Car2's brand and model:  Renault Megane 3
