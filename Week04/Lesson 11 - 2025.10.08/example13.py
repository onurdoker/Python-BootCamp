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
    super().department_lessons.append("History of Computer Engineering")
    self.department_lessons = super().department_lessons


student1 = Student("Ali", "Veli")
print(vars(student1))  # => {'name': 'Ali', 'surname': 'Veli'}
print(student1.student_lessons)  # => ['History', 'Literature']

student2 = DepartmentStudent("James", "Johnson", "Math")
print(vars(student2))  # => {'name': 'James', 'surname': 'Johnson', 'department': 'Math'}
print(student2.student_lessons)  # => ['History', 'Literature']
print(student2.department_lessons)  # => ['algorithms', 'data analysis']
