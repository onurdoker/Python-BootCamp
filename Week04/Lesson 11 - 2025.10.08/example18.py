"""
1. Public Members:

Definition: Starts with a normal name (no leading underscore)
Access: Can be accessed directly from inside the class, outside the class, or from subclasses - in other word, from anywhere
Purpose:  Represents the official interface your class exposes to the outside world. These are the attributes and methods intended to be safely
used by other parts of the program
"""


class Car:
  def __init__(self, brand, color):
    # Public attrubutes (visible and modifiable by everyone)
    self.brand = brand
    self.color = color

  def run(self):
    # Public method
    return f"The {self.color} {self.brand} is running."


# Access from outside the class
car_object = Car("Volvo", "blue")

# Direct access and modification to attributes
print(f"Brand: {car_object.brand} ")
# Brand: Volvo

# Direct modification from outside the class
print(f"Car's color: {car_object.color}")
# Car's color: blue
car_object.color = "Red"
print(f"New color: {car_object.color}")
# New color: Red

# Call the method outside the class
print(car_object.run())
# The Red Volvo is running.
