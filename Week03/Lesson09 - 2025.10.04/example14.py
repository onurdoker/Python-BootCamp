import csv

with open("students.csv", "w", encoding="UTF-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "Department"])
    writer.writerow(["Jack", 22, "Computer Engineering"])
    writer.writerow(["Jill", 40, "Chemical Engineering"])
    writer.writerow(["John", 35, "Mechanical Engineering"])
    writer.writerow(["Jill", 28, "Physics Engineering"])

# Reading CSV files
with open("students.csv", "r", encoding="UTF-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
