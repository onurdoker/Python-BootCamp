# ! First Example
"""
What is a Property

- A property allows us to use a method inside a class as if it were an attribute
- In other words, it can be called without parentheses.
- It is commonly used to control reading, writing, and deletion of an attribute
"""

from doctest import Example


# ? without @property
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height


# calculate_area = Rectangle(5, 3)
# print(calculate_area.area())  # ? have to use () after functions


# ? with @property
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     @property
#     def area(self):
#         return self.width * self.height


# calculate_area = Rectangle(5, 3)
# print(calculate_area.area)  # ? cant use ()


# ! Second Example
# class Rectangle:
#     def __init__(self, width, height):
#         self._width = width  # private value
#         self._height = height  # private value

#     @property
#     def width(self):
#         return self._width

#     @width.setter
#     def width(self, value):
#         if value > 0:
#             self._width = value
#         else:
#             print("width can't be zero or negative")


# calculate_area = Rectangle(5, 3)
# print("Width: ", calculate_area._width)

# calculate_area.width = 10
# print("new width value: ", calculate_area.width)

# calculate_area.width = -3
# print("last width value: ", calculate_area.width)


# ! Third Example
# ? First Practice
# class Animal:
#     def __init__(self,
#                  name):
#         self.name = name
#
#     def make_sound(self):
#         print('unknown voice')
#
# x = Animal('x')
# print(x.name)
# x.make_sound()


# ? Second Practice
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def make_sound(self):
#         print("unknown voice")


# class Dog(Animal):
#     def make_sound(self):
#         print("woof woof")


# dog1 = Dog("Com")
# print(dog1.name)
# dog1.make_sound()


# ? Third Practice
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def make_sound(self):
#         print("unknown voice")


# class Dog(Animal):
#     def make_sound(self):
#         print("woof woof")


# class Bird(Animal):
#     def __init__(self, name, wind_length):
#         Animal.__init__(self, name)
#         self.wind_length = wind_length

#     def make_sound(self):
#         print("chirp chirp")


#
# ciciki = Bird("ciciki",
#               2.5)
# print(ciciki.name)
# ciciki.make_sound()
# print(ciciki.wind_length)

# ? Fourth Practice
# * we use the super() method when wwe need to access the parent (super) class
# * The super() method is preferred when writing code


# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def make_sound(self):
#         print("unknown voice")


# class Dog(Animal):
#     def make_sound(self):
#         print("woof woof")


# class Bird(Animal):
#     def __init__(self, name, wind_length):
#         super().__init__(self, name)
#         self.wind_length = wind_length

#     def make_sound(self):
#         print("chirp chirp")


# ciciki = Bird("ciciki", 2.5)
# print(ciciki.name)
# ciciki.make_sound()
# print(ciciki.wind_length)

# ! Fourth Example
"""
Basic Concepts of Inheritance
- Parent class (superclass): the base class
- Child class (subclass): the class derived from parent class
- super(): used to access methods of the parent class
"""


# class Student:
#     student_lessons = ["History", "Literature"]

#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname


# class DepartmentStudent(Student):
#     department_lessons = ["algorithms", "data analysis"]

#     def __init__(self, name, surname, department):
#         super().__init__(name, surname)
#         self.department = department


# class FacultyStudent(DepartmentStudent):
#     faculty_lessons = ["History of Engineering"]

#     def __init__(self, name, surname, department, faculty):
#         super().__init__(name, surname, department)
#         self.faculty = faculty


# student1 = Student("Ali", "Veli")
# print(vars(student1))  # => {'name': 'Ali', 'surname': 'Veli'}
# print(student1.student_lessons)  # => ['History', 'Literature']

# student2 = DepartmentStudent("James", "Johnson", "Math")
# print(
#     vars(student2)
# )  # => {'name': 'James', 'surname': 'Johnson', 'department': 'Math'}
# print(student2.student_lessons)  # => ['History', 'Literature']
# print(student2.department_lessons)  # => ['algorithms', 'data analysis']


# ! Fifth Example
# class Football_Player:
#     running = "Can run"
#     sprint = "Can sprint"
#     salary = 500

#     def __init__(self, foot="right"):
#         self.foot = foot
#         self.spot = "mid-field"


# class Basketball_Player:
#     vault = "Can vault"
#     three_point_shot = "Can three-point shot"
#     salary = 750

#     def __init__(self):
#         self.spot = "offence"


# class Multi_Player(Football_Player, Basketball_Player):
#     def __init__(self, foot):
#         Basketball_Player.__init__(self)
#         Football_Player.__init__(self, foot)


# John = Multi_Player("left")
# print("Vault:", John.vault)
# print("Is John runnable ", John.running)
# print("John's salary is ", John.salary)


# ! Sixth Example
# class Employee:
#     raise_rate = 1.05
#     personal_number = 0

#     def __init__(self, name, surname, salary):
#         self.name = name
#         self.surname = surname
#         self.salary = salary
#         self.email = self.name + self.surname + "@mail.com"
#         Employee.personal_number += 1

#     def fullname(self):
#         return "Name: {} surname: {}".format(self.name, self.surname)

#     def increase(self):
#         self.salary = self.salary * self.raise_rate


# class Developer(Employee):
#     def __init__(self, name, surname, salary, programming_language):
#         super().__init__(name, surname, salary)
#         self.programming_language = programming_language
#         self.raise_rate = 1.2


# class Manager(Employee):
#     def __init__(self, name, surname, salary, employers=[]):
#         super().__init__(name, surname, salary)
#         if employers is None:
#             self.employers = []
#         else:
#             self.employers = employers

#     def add_employer(self, employer):
#         self.employers.append(employer)

#     def remove_employer(self, employer):
#         self.employers.remove(employer)

#     def print_employers(self):
#         for employer in self.employers:
#             print(employer.fullname())


# employee1 = Employee("John", "Doe", 2500)
# employee2 = Employee("Jack", "Black", 1950)

# developer1 = Developer("Black", "Jack", 2500, "Python")

# manager1 = Manager("Eric", "Match", 4000, [employee1, developer1])

# manager1.print_employers()
"""
Name: John surname: Doe
Name: Black surname: Jack
"""

# manager1.add_employer(employee2)
# manager1.print_employers()
"""
Name: John surname: Doe
Name: Black surname: Jack
Name: Jack surname: Black
"""

# manager1.remove_employer(developer1)
# manager1.print_employers()
"""
Name: John surname: Doe
Name: Jack surname: Black
"""

# print(isinstance(employee1, Manager))  # False
# print(isinstance(employee1, Developer))  # False
# print(isinstance(employee1, Employee))  # True

# print(issubclass(Employee, Developer))  # False
# print(issubclass(Developer, Employee))  # True

# ! Seventh Example
"""
Python OOP: Access Modifiers
Introduction: Why Is Access Control Needed? (Encapsulation)
Object-oriented programming (OOP) organizes programming by combining data (attributes/variables) and the function (methods) that operate on that
data into structures called class.

Access Modifiers determine whether certain data or methods within a class can be directly accessed or modified from outside the class - in other
words, whether they remain hidden or exposed.

This concept is known as Encapsulation.Its purpose is as follows:
- Security: Prevent critical data being accidentally or intentionally modified.
(Example: Preventing a bank account from being directly changed from outside the class)

- Organization: Hide the internal workings of a class from outside world, making the code easier to maintain and manage.
"""

"""
Unlike traditional OOP languages, Python does not acctually have "private" or "protected" keywords.

Instead, Python follows the philosophy of "Trust the Developer", and indicates access levels through naming conventions rather that strict
enforcement.

Here are the main conventions:
Access Level        Definition Style            Convention Name     Actual AccessBehavior
  Public            Normal name (name)          Public              Accessible from anywhere
  Protected         Single underscore (_name)   Protected           Technically accessible from anywhere, but signals "Please don't touch this from outside"
  Private           Double underscore (__name)  Private             Makes external access harder through name mangling
"""

"""
- Encapsulation in Python relies on good-faith programming conventions rather than strict rules.
- Access specifiers (modifiers) let us indicate which parts of your code are the "internal
implementation" and which are the "external interface"
- It is the foundation of writing maintainable code
"""

"""
1. Public Members:

Definition: Starts with a normal name (no leading underscore)
Access: Can be accessed directly from inside the class, outside the class, or from subclasses - in other word, from anywhere
Purpose:  Represents the official interface your class exposes to the outside world. These are the attributes and methods intended to be safely
used by other parts of the program
"""


# class Car:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color

#     def run(self):
#         return f"The {self.brand} started"


# car_object = Car("BMW", "blue")

# print(f"Brand: {car_object.brand}")  # Brand: BMW

# print(
#     f"Model: {car_object.brand} and color: {car_object.color}"
# )  # Model: BMW and color: blue

# car_object.color = "red"  # The color was changed from outside
# print(
#     f"Model: {car_object.brand} and color: {car_object.color}"
# )  # Model: BMW and color: red

# ! Eighth Example
"""
2. Protected Conventions

Definition: Begins with underscore (_)
Access: Technically, it is still accessible from anywhere - but this servers as a warning that it's meant for internal of subclass use.
Purpose: Indicates that the member belongs to the internal workings of the class. Its designed to be used by subclasses, but should not be modified directly from outside.

Important Note: Python does not enforce this restriction.
It's the developer's responsibility to respect this convention.

Example:
In a bank account, the balance should only be modified through methods like deposit() or withdraw(), not directly from outside
"""


# class BankAccount:
#     def __init__(self, account_number, balance=0):
#         self.account_number = account_number
#         self._balance = balance

#     def deposit(self, amount):
#         self._balance += amount
#         print(f"The new balance is: ${self._balance}")

#     def log(self, transaction):
#         print(f"The {self.account_number} logged {transaction}")


# account = BankAccount("12345", 1000)

# ? Proper usage (changing balance via public method)
# account.deposit(100)  # The new balance is: $1100

# ? Technically possible, but improper usage (rule violation)
# ? Python won't stop you, but this is considered bad programming practice
# account._balance = 999999
# print(f"The account balance: {account._balance}")  # The account balance: 999999

# ! Nineth Example
"""
3. Private Members:

Definition: Begins with a double underscore (__)
Access: This is the most restrictive method on Python.
Members cannot be accessed directly from outside the class.

Purpose: Used to hide the most critical or sensitive data or helper methods of a class from the outside world.

How It Works (Name Mangling)
When Python encounters an attribute or method that starts with a double underscore, it automatically changes its name
This process is called Name Mangling
__secret_date ==> _ClassName__secret_data

This prevent direct access from outside the class and attempting to do so will raise an AttributeError.
"""


# class User:
#     def __init__(self, name, password):
#         self.name = name
#         self.__password = password

#     # Private method
#     def __password_check(self):
#         return len(self.__password) > 8

#     def login(self, entered_password):
#         if self.__password_check() and entered_password == self.__password:
#             return "Logged In"
#         else:
#             return "Wrong or invalid Password"


# ? Access from outside the class
# user1 = User("John", "secret123")

# ? 1. Accessing Public Attributes
# print(user1.name)  # John

# ? 2. Accessing Private Attributes (Raise Error!!)
# try:
#     print(user1.__password)
# except AttributeError as error:
#     print(
#         f"\n[ERROR] Direct Access Blocked {error} "
#     )  # [ERROR] Direct Access Blocked 'User' object has no attribute '__password'

# ? 3. Accessing via Public Method (Proper Usage)
# print(user1.login("secret"))  # Wrong or invalid Password
# print(user1.login("secret123"))  # Logged In

# ? 4. Name Mangling (Forced Access - Should Not Be Done!)
# print(
#     f"\nAccessing via Name Mangling: {user1._User__password}"
# )  # Accessing via Name Mangling: secret123


# ! Tenth Example
# class Athlete:
#     def __init__(self, name, field, gold, silver, bronze):
#         self.name = name
#         self.field = field
#         self.mbronze = bronze  # public data
#         self._msilver = silver  # protected data
#         self.__mgold = gold  # private data

#     def athlete_info(self):
#         return "Athlete name: {}, Field: {}".format(athlete1.name, athlete1.field)

#     @property
#     def a_print(self):
#         gold_medal = self.__mgold
#         return "Number of gold medals: {}".format(self.__mgold)


# athlete1 = Athlete("John", "splinter", 2, 3, 9)

# print(athlete1.athlete_info())
"""
Athlete name: John, Field: splinter
"""

# print("Number of bronze medal: ", athlete1.mbronze)
"""
Number of bronze medal:  9
"""

# print("Number of silver medal: ", athlete1._msilver)
"""
Number of silver medal:  3
"""

# print(athlete1.a_print)
"""
Number of gold medals: 2
"""

# ! Eleventh Example
