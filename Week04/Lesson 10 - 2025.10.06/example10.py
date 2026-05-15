class Student:
    department = "Finance"
    building = "North"

    def __init__(self, name, surname, id_no):
        self.name = name
        self.surname = surname
        self.id_no = id_no

    def fullname(self):
        self.full_name = self.name + " " + self.surname
        return self.full_name


student1 = Student("Jack", "Doe", "001")
student1.fullname()
print(student1.full_name)  # Jack Doe
