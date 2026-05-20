class Employee:
  raise_rate = 1.05
  personal_number = 0

  def __init__(self, name, surname, salary):
    self.name = name
    self.surname = surname
    self.salary = salary
    self.email = self.name + self.surname + "@mail.com"
    Employee.personal_number += 1

  def fullname(self):
    return "Name: {} surname: {}".format(self.name, self.surname)

  def increase(self):
    # self.salary = self.salary * 1.05  # manuel definition
    # self.salary = self.salary * Employee.raise_rate  # Class-based definition
    self.salary = self.salary * self.raise_rate  # Instance-based definition


class Developer(Employee):
  def __init__(self, name, surname, salary, programming_language):
    super().__init__(name, surname, salary)
    self.programming_language = programming_language
    self.raise_rate = 1.20


class Manager(Employee):
  def __init__(self, name, surname, salary, employees=None):
    super().__init__(name, surname, salary)
    if employees is None:
      self.employees = []
    else:
      self.employees = employees

  def add_employee(self, employer):
    self.employees.append(employer)

  def remove_employee(self, employer):
    self.employees.remove(employer)

  def show_employees(self):
    for employee in self.employees:
      print(employee.fullname())


person1 = Employee("Jack", "Dow", 2500)
person2 = Employee("Jane", "Black", 1950)

developer1 = Developer("Jill", "Smith", 2250, "Python")

manager1 = Manager("Jim", "Scott", 6500, [person1, developer1])

manager1.show_employees()
# Name: Jack surname: Dow
# Name: Jill surname: Smith

manager1.add_employee(person2)
manager1.show_employees()
# Name: Jack surname: Dow
# Name: Jill surname: Smith
# Name: Jane surname: Black

print(manager1.fullname())
# Name: Jim surname: Scott

manager1.remove_employee(developer1)
manager1.show_employees()
# Name: Jack surname: Dow
# Name: Jane surname: Black

print(isinstance(person1, Manager))  # False
print(isinstance(person1, Developer))  # False
print(isinstance(person1, Employee))  # True


print(issubclass(Developer, Employee))  # True
