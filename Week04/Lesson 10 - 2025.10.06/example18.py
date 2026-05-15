class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def increase(self, ratio):
        self.width *= ratio
        self.height *= ratio
        return f"New width: {self.width}; \nNew height: {self.height}"


rectangle1 = Rectangle(5, 3)
print(f"Area of the rectangle: {rectangle1.area()} ")  # Area of the rectangle: 15
print(
    f"Perimeter of the rectangle: {rectangle1.perimeter()}"
)  # Perimeter of the rectangle: 16

rectangle1.increase(2)
print(f"Area of the rectangle: {rectangle1.area()}: ")  # Area of the rectangle: 60:
