"""
Convert csv to dictionary
"""

import csv

with open("students.csv", "w", encoding="UTF-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "Department"])
    writer.writerow(["Jack", 22, "Computer Engineering"])
    writer.writerow(["Jill", 40, "Chemical Engineering"])
    writer.writerow(["John", 35, "Mechanical Engineering"])
    writer.writerow(["Jill", 28, "Physics Engineering"])


with open("students.csv", "r", encoding="UTF-8") as file:
    field_names = file.readline().strip().split(",")
    # print(field_names)
    for row in file:
        line = row.strip().split(",")
        # print(line)
        student = dict(zip(field_names, line))
        print(student)
