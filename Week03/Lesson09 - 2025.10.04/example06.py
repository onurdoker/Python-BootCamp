"""
! File operations in Python

There is three file types
1. Text File
2. CSV File => Comma Separated Values
3. JSON File => JavaScript Object Notation (Web, API etc.)
"""

name = "Jack"
age = 40

# * Text File
# ? Step 1. Open file from writing mode
file = open("file.txt", "w")

# ? Step 2. Add string into file
file.write(f"Name: {name}\nAge: {age}")


# ? Step 3. Close file
file.close()

# ?  if you don't close the file, it will be locked, and it can cause a problem

# # if you don't want to close file, you can use 'with' statement
# with open("file.txt", "w") as file:
#     file.write(f"Name: {name}\nAge: {age}")

"""
File opening modes
'w' => write => if file exists, it will be overwritten if file doesn't exist, it will be created
'a' => append => if file exists, it will be appended if file doesn't exist, it will be created
'r' => read => if file exists, it will be read if file doesn't exist, it will raise an error
'x' => exclusive => if file exists, it will raise an error if file doesn't exist, it will be created

t => text mode (default)
b => binary mode (like picture, music files)
"""

"""
import os
folder_path = os.path.dirname(os.path.abspath(__file__))
file_path = folder_path + '/' + 'file_name.txt'
"""
