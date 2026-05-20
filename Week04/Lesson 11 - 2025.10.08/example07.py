class Rectangle:
  def __init__(self, width, height):
    self._width = width  # private value
    self.height = height

  @property  # get getter
  def width(self):
    return self._width

  @width.setter  # setter
  def width(self, value):
    if value > 0:
      self._width = value
    else:
      print("Width must be positive.")


rect = Rectangle(5, 3)
print(rect.width)  # 5

rect.width = 10
print(rect.width)  # 10

rect.width = -2
print(rect.width)  # Width must be positive. width remains 10
