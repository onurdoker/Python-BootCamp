# ! First Example

# * OOP - Object-Oriented Programming
"""
Difference from structured programming: Code reusability, modularity and ease of maintenance.
Real-world analogy: objects -> attributes + behaviors (methods)
In Python, everything is an object - even types like int, str, and list are objects
"""
from curses.textpad import rectangle

from sympy.codegen.fnodes import product_

# * Functional approach before OOP
# def student_create(name,
#                    age,
#                    average):
#     return {'name': name, 'age': age, 'average': average}
#
# def student_info(student):
#     return f"{student['name']}, {student['age']} years old, {student['average']} average"
#
# student = student_create('Onur',
#                          48,
#                          3.7)
# print(student_info(student))

# ! Second Example
# def student_info_update(student,
#                         **kwargs):
#     for key, value in kwargs.items():
#         if key in student:
#             student[key] = value
#     return student
#
# student_info_update(student,
#                     age=38)
# print(student_info(student))

# ! Third Example
# * Class
"""
Class definition: It is a blueprint for objects, specifying what attributes and functions (methods) the objects can have
"""

# class Student:
#     def __init__(self,
#                  name,
#                  age,
#                  average):
#         self.name = name
#         self.age = age
#         self.average = average
#
#     def student_info(self):
#         return f"{self.name}, {self.age} years old, {self.average} average"
#
# student1 = Student('Onur',
#                    48,
#                    3.7)
#
# print(student1.student_info())
#
# student2 = Student('Timur',
#                    57,
#                    3.9)
# print(student2.student_info())

# ! Forth Example
# * Common usage
# class Car:
#     pass
#
# car1 = Car()
# car2 = Car()

# class Student:
#     pass
#
# student1 = Student()
# student1.name = "Onur"
#
# print(student1,
#       type(student1))
# print(student1.name,
#       type(student1.name))
#
# student2 = Student()
# print("Type of student2: ",
#       type(student2))
#
# student2.name = 'John'
# student2.surname = 'Smith'
# print('Student2: ',
#       student2.name,
#       student2.surname)

# ! Fifth Example
"""
Attributes
Instance attributes: defined with self; they are unique to each object
Class attributes: defined at the class level and shared by all objects
"""

# class Car:
#     wheel_number = 4  # class attribute
#
# class Student:
#     course = 'Python 80-hour Bootcamp'
#     faculty = ''
#
# print("Number of wheel: ",
#       Car.wheel_number)
# print("General usage of Student.course: ",
#       Student.course)
#
# student1 = Student()
# print("Course of student1:",
#       student1.course)
# student1.faculty = 'Chemical Engineering'
# print("Student1's Faculty: ",
#       student1.faculty)
# print("Student's Faculty: ",
#       Student.faculty)

# ! Sixth Example
# class Book:
#     name = ''
#     author = ''
#     page_number = 0
#     publisher = ''
#     print_year = ''
#
# book1 = Book()
# book1.name = 'Animal Farm'
# book1.author = 'George Orwell'
# book1.page_number = 80
# book1.publisher = 'TechIstanbul'
# book1.print_year = 1950
#
# print("Book's name:",
#       book1.name)
#
# variables = vars(book1)
# print("Variables of books: ",
#       variables,
#       "\nType of book: ",
#       type(variables))

# ! Seventh Example
"""
__init__ => constructor method
It is automatically called when an object is created.
Defines the initial state (attributes)

self => instance
"""

# class Car:
#     wheel_number = 4  # class attribute
#
#     def __init__(self,
#                  brand,
#                  model):
#         self.brand = brand
#         self.model = model
#
# car1 = Car("Volkswagen",
#            "Golf")
# print("Car1's wheel number: ",
#       car1.wheel_number)
# print("Car1's brand and model: ",
#       car1.brand,
#       car1.model)
# car2 = Car('Renault',
#            'Megane 3')
# print("Car2's wheel number: ",
#       car2.wheel_number)
# print("Car2's brand and model: ",
#       car2.brand,
#       car2.model)
# car3 = Car(model='Civic',
#            brand='Honda')
# print("Car3's wheel number: ",
#       car3.wheel_number)
# print("Car3's brand and model: ",
#       car3.brand,
#       car3.model)

# ! Eighth Example
# * First Practice
# class Student:
#     department = 'Finance'
#     building = 'North'
#
#     def __init__(self):
#         self.name = ''
#         self.surname = ''
#         self.id_no = ''
#
# student1 = Student()
# print("Department of Student1: ",
#       student1.department)
#
# student1.name = 'Onur'
# print("Name of Student1: ",
#       student1.name)
#
# student2 = Student()
# print("Name of student2: ",
#       student2.name)
#
# print("Department and Building of Student: ",
#       Student.department,
#       Student.building)

# * Second Practice
# class Student:
#     department = 'Finance'
#     building = 'North'
#
#     def __init__(self,
#                  name,
#                  surname,
#                  id_no):
#         self.name = name
#         self.surname = surname
#         self.id_no = id_no
#
# student1 = Student("Onur",
#                    "DOKER",
#                    32232234)
# print("Department of Student1: ",
#       student1.department)
# print("Name of Student1: ",
#       student1.name)

# * Third Practice
# class Student:
#     department = 'Finance'
#     building = 'North'
#
#     def __init__(self,
#                  name,
#                  surname,
#                  id_no):
#         self.name = name
#         self.surname = surname
#         self.id_no = id_no
#
#     def fullname(self):
#         self.fullname = self.name + ' ' + self.surname
#         return self.fullname
#
#     def __str__(self):
#         return self.name + ' ' + self.surname
#
# student1 = Student("Onur",
#                    "DOKER",
#                    32232234)
#
# print("Name of Student1: ",
#       student1.name)
# student1.fullname()
# print("Full name of Student1: ",
#       student1.fullname)
#
# print(student1)

# ! Nineth Example
"""
Methods
Functions defined within a class
The self parameter is mandatory (automatically passed)

Self Keyword
Every method takes self as its first parameter
in Python, self is automatically passed when calling object,method().
You can use a different name instead of self, but it is not considered best practices
"""

"""
|===================|===========|=======================|===============================|===============================================|
|   Type            | Parameter |    Accessible         |    Call Location              |    Purpose                                    |
|===================|===========|=======================|===============================|===============================================|
| Instance method   | self      | Instance variables    | Using the object              | Methods define object-specific operations     |
| Class method      | cls       | Class variables       | Via the class or the object   | Operations related to all classes             |
| Static method     |           | None of them          | Via the class or the object   | Helper functions                              |
|===================|===========|=======================|===============================|===============================================|

"""

# ? Instance Method
"""
1. Normal (Instance) Methods
- These are methods that belong to an object (instance) created from a class
- The first parameter must be self, which represents the object itself
"""

# class Student:
#     def __init__(self,
#                  name,
#                  age):
#         self.name = name
#         self.age = age
#
#     def show_info(self):
#         print(f"Name: {self.name}, \nAge: {self.age}")
#
# student1 = Student("John",
#                    22)
# student1.show_info()

"""
__init__ is a constructor method. It is automatically called when an object is created.
show_info is a normal (instance) method; it accesses object data through self
"""

# ? Class method

"""
2. Class methods
- These are methods that belong to an object (instance) created from a class, not to an instance.
- It takes cls as its first parameter (representing the class)

- Defined using the @classmethod decorator
"""

# class Student:
#     school_name = "TechIstanbul Academy"
#
#     def __init__(self,
#                  name,
#                  age):
#         self.name = name
#         self.age = age
#
#     @classmethod
#     def school_info(cls):
#         print(f"This students go to {cls.school_name}")
#
#     def student_school_info(self):
#         print(f"The current school information of this student: {self.school_name}")
#
# Student.school_info()  # => This students go to TechIstanbul Academy
#
# student1 = Student('Alex',
#                    22)
# student1.school_info()  # => This students go to TechIstanbul Academy
#
# student1.school_name = 'Yale University'
# student1.school_info()  # => This students go to TechIstanbul Academy
# student1.student_school_info()  # => The current school information of this student: Yale University
#
# student2 = Student('Tom',
#                    66)
# student2.school_info()  # => This students go to TechIstanbul Academy
# student2.student_school_info()  # => The current school information of this student: TechIstanbul Academy


# ? Static Methods
"""
3. Static methods (@staticmethod)
- These methods are bound neither to the class nor to the instance.
- They behave like independent functions but are defined within a class.

- They are defined using the @staticmethod decorator and do not take self or cls as a parameter 
"""

# class Mathematics:
#     @staticmethod
#     def sum(a,
#             b):
#         return a + b
#
#     @staticmethod
#     def multiply(a,
#                  b):
#         return a * b
#
# print(Mathematics.sum(5,
#                       3))
# print(Mathematics.multiply(5,
#                            2))

"""
- They are ideal for helper (utility) operations
- They do not take self or cls because they cannot access instance or class data
"""

# !  Tenth Example
# class Worker:
#     raise_ratio = 1.1
#
#     def __init__(self,
#                  name,
#                  salary):
#         self.name = name
#         self.salary = salary
#
# # Instance method
#     def show_salary(self):
#         print(f"{self.name} salary: {self.salary} $")
#
# # Class method
#     @classmethod
#     def do_raise(cls,
#                  rate):
#         cls.raise_ratio = rate
#         print(f"New raise ratio: {cls.raise_ratio}")
#
# # Static method
#     @staticmethod
#     def info():
#         print("This class manages the salaries of employees")
#
# Worker.info()
# Worker.do_raise(1.2)
# worker1 = Worker(name="John",
#                  salary=20000)
# worker1.show_salary()

# ! Eleventh Example
# class Student:
#     school_name = "TechIstanbul"
#     number_of_students = 0
#
#     def __init__(self,
#                  name,
#                  surname,
#                  average):
#         self.name = name
#         self.surname = surname
#         self.average = average
#         Student.number_of_students += 1
#
#     # Instance Method
#     def show_info(self):
#         print(f"{self.name} {self.surname} - Average: {self.average}")
#
#     # Class Method
#     @classmethod
#     def school_info(self):
#         print(f"{self.school_name}, Total Students: {Student.number_of_students}")
#
#     # Static Method
#     @staticmethod
#     def calculate_average(grades):
#         return sum(grades) / Student.number_of_students if grades else 0
#
# # Adding students
# student1 = Student("James",
#                    "Smith",
#                    90)
# student2 = Student("Damla",
#                    "ALKAN",
#                    100)
# student3 = Student("Onur",
#                    "DOKER",
#                    90)
#
# print(f"Number of registered students: {student1.number_of_students}")  # => Number of registered students: 3
#
# # School Info (Class method)
# Student.school_info()  # => TechIstanbul, Total Students: 3
# student1.show_info()  # => James Smith - Average: 90
#
# # Calculating Average (Static method)
# grades = [student1.average,
#           student2.average,
#           student3.average]
# general_average = Student.calculate_average(grades)
# print(f"General average: {general_average:.02f}")


# ! Twentieth Example
# ? First Practice
# class Car:
#     def __init__(self,
#                  brand,
#                  model,
#                  year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.velocity = 0
#
#     def show_info(self):
#         return f"{self.year} {self.brand} {self.model}, Velocity: {self.velocity} km/s"
#
#     def accelerate(self,
#                    amount):
#         self.velocity += amount
#         return f"The car accelerated, new velocity: {self.velocity} km/s"
#
#     def decelerate(self,
#                    amount):
#         self.velocity -= amount
#         return f"The car decelerated, new velocity: {self.velocity} km/s"
#
# car1 = Car('Toyota',
#            "Corolla",
#            2022)
# car2 = Car('Honda',
#            'Civic',
#            2023)
#
# print(car1.show_info())
# print(car2.show_info())
#
# car1.accelerate(100)
# print(car1.show_info())
#
# car1.decelerate(30)
# print(car1.show_info())

# ? Second Practice
# class Car:
#     velocity = 0
#
#     def __init__(self,
#                  brand,
#                  model,
#                  year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.velocity = Car.velocity
#
#     def show_info(self):
#         return f"{self.year} {self.brand} {self.model}, Velocity: {self.velocity} km/s"
#
#     def accelerate(self,
#                    amount):
#         self.velocity += amount
#         return f"The car accelerated, new velocity: {self.velocity} km/s"
#
#     def decelerate(self,
#                    amount):
#         self.velocity -= amount
#         return f"The car decelerated, new velocity: {self.velocity} km/s"
#
#     @classmethod
#     def shared_velocity(cls,
#                         amount):
#         cls.velocity += amount
#
# car1 = Car('Toyota',
#            "Corolla",
#            2022)
# car2 = Car('Honda',
#            'Civic',
#            2023)
#
# print(car1.show_info())
#
# Car.shared_velocity(100)
# car3 = Car('BWM',
#            '1 series',
#            2023)
# print(car3.show_info())


# ! Thirtieth Example
# class Bill():
#     header = "Halil Marketing"
#     payment = True
#     content = {}
#
#     def __init__(self,
#                  mName,
#                  tax_number,
#                  date):
#         self.mName = mName
#         self.tax_number = tax_number
#         self.date = date
#         self.total = 0
#
#     def add_product(self):
#         product_name = input('Please enter the product name: ')
#         product_quantity = int(input('Please enter the product quantity: '))
#         product_price = float(input('Please enter the unit price od product: '))
#         product_amount = product_quantity * product_price
#         self.content[product_name] = [product_amount,
#                                       product_price,
#                                       product_amount]
#         self.total += product_amount
#         print(f"{self.content[product_name]} has been added to the cart")
#         return self.invoice_amount()
#
#     def remove_product(self):
#         product_name = input('Please enter the product name: ')
#         product_amount = self.content[product_name][2]
#         self.total -= product_amount
#         print(f"{self.content[product_name]} has been removed to the cart")
#         del self.content[product_name]
#         return self.invoice_amount()
#
#     def invoice_amount(self):
#         print("Current invoice amount: {:.2f}".format(self.total))
#         return self.total
#
# customer = Bill("Damla",
#                 123456,
#                 2024)
# customer.add_product()

# ! Fourteenth Example
# class Rectangle:
#
#     def __init__(self,
#                  width,
#                  height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#
#     def increase(self,
#                  ratio):
#         self.width *= ratio
#         self.height *= ratio
#         return f"New width: {self.width}; \nNew height: {self.height}"
#
# rectangle1 = Rectangle(5,
#                        3)
# print(f"Area of the rectangle: {rectangle1.area()}: ")
# print(f"Perimeter of the rectangle: {rectangle1.perimeter()}")
#
# rectangle1.increase(2)
# print(f"Area of the rectangle: {rectangle1.area()}: ")

# ! Fifteenth Example
# class Book:
#     def __init__(self,
#                  isbn,
#                  title,
#                  author,
#                  pages,
#                  year):
#         self.isbn = isbn
#         self.title = title
#         self.author = author
#         self.pages = pages
#         self.year = year
#         self.borrowed = False
#
#     def do_borrow(self):
#         if not self.borrowed:
#             self.borrowed = True
#             return f"{self.title} borrowed"
#         else:
#             return f"{self.title} already borrowed"
#
#     def do_return(self):
#         if not self.borrowed:
#             self.borrowed = False
#             return f"{self.title} returned"
#         else:
#             return f"{self.title} already returned"
#
#     def book_info(self):
#         status = "Borrowed" if self.borrowed else "Not Borrowed"
#         return f"ISBN: {self.isbn} \nTitle: {self.title} \nAuthor: {self.author} \nPages: {self.pages} \nYear: {self.year} \nStatus: {status}"
#
# class Library:
#
#     def __init__(self,
#                  name):
#         self.name = name
#         self.books = []
#
#     def add_book(self,
#                  book):
#         self.books.append(book)
#         return f"{book.title} has been added to the library"
#
#     def search_book(self,
#                     key_word):
#         find_books = []
#         for book in self.books:
#             if (key_word.lower() in book.title.lower() or key_word.lower() in book.author.lower()):
#                 find_books.append(book)
#         return find_books
#
#     def available_books(self):
#         return [book for book in self.books if not book.do_borrow]
#
#     def borrowed_books(self):
#         return [book for book in self.books if book.do_borrow]
#
#     def library_info(self):
#         total = len(self.books)
#         borrowed = len(self.borrowed_books())
#         available = len(self.available_books())
#
#         report = f"=== {self.name} ===\n"
#         report += f"Total Books: {total}\n"
#         report += f"Available Books: {available}\n"
#         report += f"Borrowed Books: {borrowed}\n"
#         return report
#
# # Usage
# library = Library("Main Library")
#
# # Adding books
# book1 = Book("123456",
#              "Python Programming",
#              "Ahmet Emin",
#              350,
#              2023)
#
# book2 = Book("987654",
#              "Data Science",
#              "John Doe",
#              230,
#              2022)
#
# # Adding books
# library.add_book(book1)
# library.add_book(book2)
# print(book1.book_info())
#
# print(library.library_info())
#
# # Borrow a book
# print(book1.do_borrow())
# print(library.library_info())
# print(book2.book_info())

# ! Sixteenth Example
"""
Decorators:

Decorators are function in Python that wrap another function and modify its behavior.

in other words, a decorator adds extra functionality before or after a function executes.
"""

# * without decorator
# def greeting():
#     print("Hello, world!")
#
# greeting()

# ? First practice
"""
General decorator usage

def decorator(function):
    def wrapper():
        print("Before function calling")
        function()
        print("After function calling")
    return wrapper
    
@decorator
def greeting():
    print("Hello, world!")

greeting()
"""

# def changecase(function):
#     def myinner():
#         return function().upper()
#
#     return myinner
#
# @changecase
# def myfunction():
#     return "hello world!"
#
# @changecase
# def otherfunction():
#     return "Python Bootcamp"
#
# print(myfunction())
# print(otherfunction())


# !  Seventeenth Example
# * Usage with functions that take parameters

"""
If the function to be decorated takes parameters, the wrapper function must also take those parameters

def decorator(function):
    def wrapper(*args, **kwargs):
        print("Before function calling")
        function(*args, **kwargs)
        print("After function calling")
    return wrapper

@decorator
def function(*args, **kwargs):
   print("Function calling")

function(*args, **kwargs)
"""

# def changecase(n):
#     def changecase(function):
#         def myinner():
#             if n == 1:
#                 a = function().lower()
#             else:
#                 a = function().upper()
#             return a
#
#         return myinner
#
#     return changecase
#
# @changecase(2)
# def myfunction():
#     return "Function calling"
#
# print(myfunction())
