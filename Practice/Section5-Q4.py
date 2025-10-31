"""
Create a student ID Card. After asking the student for information such as first name, last name, ask for their courses and grades for those courses,
and write system that gives a collective output.
"""


class Student:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.student_id = ""
        self.department = ""
        self.courses = []

    def student_info(self):
        print("========== STUDENT INFORMATION FORM ==========")

        self.first_name = input("Please enter your first name: ").capitalize()
        self.last_name = input("Please enter your last name: ").upper()
        self.student_id = int(input("Please your student ID (numerical only): "))
        self.department = input("Please enter your Department: ").capitalize()

    def add_course(self):
        print("========== ADDING COURSE AND GRADE FORM ==========")

        while True:
            try:
                number_course = int(
                    input("How many courses do you want to add (only numerical): ")
                )
                if number_course <= 0:
                    print("Please enter a valid number")
                else:
                    for i in range(number_course):
                        print(f"\nCourse {i+1}:")
                        course_code = input("Please enter course code: ").upper()
                        course_name = input("Please enter course name: ").capitalize()

                        while True:
                            try:
                                credits = int(input("Please enter course credit: "))
                                if credits > 0:
                                    break
                                else:
                                    print("Credits must be positive number!")
                            except ValueError:
                                print("Please enter a valid number")

                        while True:
                            try:
                                grade = float(
                                    input("Please enter grade (between 0 and 100): ")
                                )
                                if 0 <= grade <= 100:
                                    break
                                else:
                                    print("Grade must be between 0 and 100!")
                                pass
                            except ValueError:
                                print("Please enter a valid number")

                        course = {
                            "course_code": course_code,
                            "course_name": course_name,
                            "credits": credits,
                            "grade": grade,
                        }
                        self.courses.append(course)

                    print("Courses added successfully")

                    break
            except ValueError:
                print("Please enter a valid number")

    def display_student_card(self):
        print("========== STUDENT CARD ==========")

        print("========== PERSONAL INFORMATION ==========")
        print(f"Name                    : {self.first_name} {self.last_name}")
        print(f"Student ID              : {self.student_id}")
        print(f"Department              : {self.department}")
        print(f"Total Courses           : {len(self.courses)}")

        print("\n========== COURSES ==========")
        if self.courses:
            for course in self.courses:
                print(f"\nCourse Code     : {course['course_code']}")
                print(f"Course Name     : {course['course_name']}")
                print(f"Credits         : {course['credits']}")
                print(f"Grade           : {course['grade']}")


if __name__ == "__main__":
    student = Student()

    while True:
        print("\n========== MENU ==========")
        print("1. Student Information")
        print("2. Add Course")
        print("3. Display Student Card")
        print("4. Exit")

        choice = input("Please enter your choice: ")

        if choice == "1":
            student.student_info()
        elif choice == "2":
            student.add_course()
        elif choice == "3":
            student.display_student_card()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")
