class Student:
    department = "Finance"
    building = "North"

    def __init__(self, name, surname, id_no):
        self.name = name
        self.surname = surname
        self.id_no = id_no


# student1 = Student()
# TypeError: Student.__init__() missing 3 required positional arguments: 'name', 'surname', and 'id_no'
student1 = Student("Jack", "Doe", "001")

print("Department of Student: ", student1.department)
# Department of Student:  Finance

student1.name = "Jack"
print("Name and Surname of Student1: ", student1.name, student1.surname)
# Name and Surname of Student1:  Jack Doe

student2 = Student("Jill", "Smith", "002")
print("Name of Student2: ", student2.name)
# Name of Student2:  Jill

print("Department and Building of Student2: ", student2.department, student2.building)
# Department and Building of Student2:  Finance North
