""" """


class Worker:
    raise_ratio = 1.1

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Instance method
    def show_salary(self):
        print(f"{self.name} salary: {self.salary} $")

    # Class method
    @classmethod
    def do_raise(cls, rate):
        cls.raise_ratio = rate
        print(f"New raise ratio: {cls.raise_ratio}")

    # Static method
    @staticmethod
    def info():
        print("This class manages the salaries of employees")


Worker.info()  # This class manages the salaries of employees
Worker.do_raise(1.2)  # New raise ratio: 1.2

worker1 = Worker(name="John", salary=20000)
worker1.show_salary()  # John salary: 20000 $
