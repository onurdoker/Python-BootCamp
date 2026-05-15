class Student:
    school_name = "TechIstanbul"
    number_of_students = 0

    def __init__(self, name, surname, average):
        self.name = name
        self.surname = surname
        self.average = average
        Student.number_of_students += 1

    # Instance Method
    def show_info(self):
        print(f"{self.name} {self.surname} - Average: {self.average}")

    # Class Method
    @classmethod
    def school_info(cls):
        print(f"{cls.school_name}, Total Students: {Student.number_of_students}")

    # Static Method
    @staticmethod
    def calculate_average(grades):
        return sum(grades) / Student.number_of_students if grades else 0


# Adding students
student1 = Student("Jack", "Dow", 100)
student2 = Student("Jill", "Smith", 90)
student3 = Student("James", "Smith", 80)

print(
    f"Number of registered students: {student1.number_of_students}"
)  # => Number of registered students: 3

# School Info (Class method)
Student.school_info()  # => TechIstanbul, Total Students: 3
student1.show_info()  # => Jack Dow - Average: 100

# Calculating Average (Static method)
grades = [student1.average, student2.average, student3.average]
general_average = Student.calculate_average(grades)
print(f"General average: {general_average:.02f}")  # General average: 90.00
