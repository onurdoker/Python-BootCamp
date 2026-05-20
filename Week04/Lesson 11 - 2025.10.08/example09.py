class Animal:
  def __init__(self, name):
    self.name = name

  def make_sound(self):
    print("unknown sound")


x = Animal("x")
print(x.name)  # x
x.make_sound()  # unknown sound
