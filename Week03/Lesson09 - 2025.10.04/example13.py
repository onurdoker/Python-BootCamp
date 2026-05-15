"""
CSV Files
"""

with open("students.csv", "w", encoding="utf-8") as file:
    file.write("Name, Age, Department\n")
    file.write("Jack, 22, Computer Engineering\n")
    file.write("Jill, 40, Chemical Engineering\n")
    file.write("John, 35, Mechanical Engineering\n")
    file.write("Jill, 28, Physics Engineering\n")

with open("students.csv", "r", encoding="UTF-8") as file:
    for lines in file:
        print(lines.strip())
