class Animal:
  def __init__(self, name):
    self.name = name

  def make_sound(self):
    print("unknown sound")


class Dog(Animal):
  def make_sound(self):
    print("Woof woof")


dog1 = Dog("Com")
print(dog1.name)  # Com
dog1.make_sound()  # Woof woof
