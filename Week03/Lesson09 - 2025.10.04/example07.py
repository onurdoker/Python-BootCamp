"""
Reading data from file
"""

# file = open("file2.txt", "r")  # Error => FileNorFoundError
file = open("file.txt", "r")

print(file.read(10))  # Read first 10 characters
print(file.read())  # Read rest off the File
