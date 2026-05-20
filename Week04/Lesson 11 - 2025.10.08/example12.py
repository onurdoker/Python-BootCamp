"""
Basic Concepts of Inheritance
- Parent class (superclass): the base class
- Child class (subclass): the class derived from parent class
- super(): used to access methods of the parent class
"""


class Student:
  student_lessons = ["History", "Literature"]

  def __init__(self, name, surname):
    self.name = name
    self.surname = surname


class DepartmentStudent(Student):
  department_lessons = ["algorithms", "data analysis"]

  def __init__(self, name, surname, department):
    super().__init__(name, surname)
    self.department = department


class FacultyStudent(DepartmentStudent):
  faculty_lessons = ["History of Engineering"]

  def __init__(self, name, surname, department, faculty):
    super().__init__(name, surname, department)
    self.faculty = faculty


student1 = Student("Ali", "Veli")
print(vars(student1))  # => {'name': 'Ali', 'surname': 'Veli'}
print(student1.student_lessons)  # => ['History', 'Literature']

student2 = DepartmentStudent("James", "Johnson", "Math")
print(vars(student2))  # => {'name': 'James', 'surname': 'Johnson', 'department': 'Math'}
print(student2.student_lessons)  # => ['History', 'Literature']
print(student2.department_lessons)  # => ['algorithms', 'data analysis']
