class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.velocity = 0

    def show_info(self):
        return f"{self.year} {self.brand} {self.model}, Velocity: {self.velocity} km/s"

    def accelerate(self, amount):
        self.velocity += amount
        return f"The car accelerated, new velocity: {self.velocity} km/s"

    def decelerate(self, amount):
        self.velocity -= amount
        return f"The car decelerated, new velocity: {self.velocity} km/s"


car1 = Car("Toyota", "Corolla", 2022)
car2 = Car("Honda", "Civic", 2023)

print(car1.show_info())  # 2022 Toyota Corolla, Velocity: 0 km/s
print(car2.show_info())  # 2023 Honda Civic, Velocity: 0 km/s

car1.accelerate(100)  # The car accelerated, new velocity: 100 km/s
print(car1.show_info())  # 2022 Toyota Corolla, Velocity: 100 km/s

car1.decelerate(30)  # The car decelerated, new velocity: 70 km/s
print(car1.show_info())  # 2022 Toyota Corolla, Velocity: 70 km/s
