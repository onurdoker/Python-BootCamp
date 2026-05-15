"""
Create a file, write data to it, read from the file, and write back to it.
"""

text = "Python BootCamp by TechIstanbul is too good.\n"

file2 = open("file2.txt", "w", encoding="utf-8")

file2.write(text)
file2.close()

# Adding more text to the file
with open("file2.txt", "a", encoding="utf-8") as file:
    file.write("This course held 80 hours.\n")

# Reading from the file
with open("file2.txt", "r", encoding="utf-8") as file:
    print(file.read())
