"""
We use the super() method when wwe need to access the parent (super) class
The super() method is preferred when writing code
"""


class Animal:
  def __init__(self, name):
    self.name = name

  def make_sound(self):
    print("unknown sound")


class Dog(Animal):
  def make_sound(self):
    print("Woof woof")


class Bird(Animal):
  def __init__(self, name, wind_length):
    # Animal.__init__(self, name)
    super().__init__(name)  # super().__init__(self, name) also works here!
    self.wind_lenght = wind_length

  def fly(self):
    print("Bird flying")


Ciciki = Bird("Ciciki", 2.5)
print(vars(Ciciki))  # {'name': 'Ciciki', 'wind_lenght': 2.5}
Ciciki.make_sound()  # unknown sound
Ciciki.fly()  # Bird fling
