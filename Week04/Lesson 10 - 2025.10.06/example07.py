class Student:
    department = "Finance"
    building = "North"

    def __init__(self):
        self.name = ""
        self.surname = ""
        self.id_no = ""


student1 = Student()
print("Department of Student: ", student1.department)
# Department of Student:  Finance

student1.name = "Jack"
print("Name of Student1: ", student1.name)
# Name of Student1:  Jack

student2 = Student()
print("Name of Student2: ", student2.name)
# Name of Student2:

print("Department and Building of Student2: ", student2.department, student2.building)
# Department and Building of Student2:  Finance North
