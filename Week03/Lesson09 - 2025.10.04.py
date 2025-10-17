# ! First Example
# * Local Scope
"""
x parameter define in function. It is not accessible outside the function
"""
# def function():
#     x = 500
#     print(x)
#
# function()
# print(x)  # NameError: name 'x' is not defined

# * Scope in functions and subfunction (Enclosing Scope)
"""
x parameter define in function. It is accessible inside the function and sub-functions,
but you can't change value of x in subfunction
"""
# def function():
#     x = 300
#
#     def subfunction():
#         print(x)
#         # x = 400  # UnboundLocalError: local variable 'x' referenced before assignment
#
#     subfunction()
#
# function()

# * Global Scope
"""
x parameter define outside function. It is accessible inside the function
"""
# x = 300
#
# def function():
#     print('inside function',
#           x)
#
# print('outside function, before function',
#       x)
# function()
# print('outside function, after function',
#       x)

"""
while in function, defined x value firstly checked in scope of function after than global scope
"""
# x = 300
#
# def function():
#     x = 500
#     print('inside function',
#           x)
#
# print('outside function, before function',
#       x)
# function()
# print('outside function, after function',
#       x)

# * Global Keyword
"""
global keyword is used to modify global variable inside function
"""

# x = 300
#
# def function():
#     global x
#     x = 500
#     print('inside function',
#           x)
#
# print('outside function, before function',
#       x)
# function()
# print('outside function, after function',
#       x)

# def function():
#     global number_
#     number_ = 500
#     print('inside function',
#           number_)
#
# function()
# print('outside function, after function',
#       number_)

"""
Global Keyword is used to modify global variable inside function
"""
# number = 300
#
# def function():
#     global number
#     number = 500 * 2
#     print('inside function',
#           number)
#
# print('outside function, before function',
#       number)
# function()
# print('outside function, after function',
#       number)


# * Nonlocal Keyword
"""
nonlocal keyword is used to modify nonlocal variable inside function
"""
# def function():
#     name = 'John'
#
#     def subfunction():
#         nonlocal name
#         name = 'Jane'
#
#     print('inside function, before subfunction',
#           name)
#     subfunction()
#     print('inside function after subfunction',
#           name)
#     return name
#
# function()

# ! Second Example
# * File
"""
There is three file types
1. Text File
2. CSV File => Comma Separated Values
3. JSON File => JavaScript Object Notation (Web, API etc.)
"""
# name = 'Timur'
# age = 57
#
# # * Text File
# # ? Step 1. Open file for writing mode
# file = open('file.txt',
#             'w')
# # ? Step 2. Add string into file
# file.write(f'Name: {name}\nAge: {age}')
# # ? Step 3. Close file
# file.close()
# # ?  if you don't close the file, it will be locked, and it can cause a problem
#
# # if you don't want to close file, you can use 'with' statement
# with open('file.txt',
#           'w') as file:
#     file.write(f'Name: {name}\nAge: {age}')

"""
File opening modes
'w' => write => if file exists, it will be overwritten if file doesn't exist, it will be created
'a' => append => if file exists, it will be appended if file doesn't exist, it will be created
'r' => read => if file exists, it will be read if file doesn't exist, it will raise an error
'x' => exclusive => if file exists, it will raise an error if file doesn't exist, it will be created

t => text mode (default)
b => binary mode (like picture, music files)
"""

# ! Third Example
# * Reading data from file

# file = open('file2.txt',
#             'r')  # Error => FileNotFoundError

# with open('file.txt',
#           'r') as file:
#     print(file.read(10))  # Read first 10 characters
#     print(file.read())  # Read rest of the file

# with open("file.txt",
#           "r") as file:
#     content1 = file.read()
#     print(f'content1: \n{content1} \ntype of content1: {type(content1)} \nlength of content1: {len(content1)}')
#
#     content2 = file.read()
#     print(f'content2: \n{content2} \ntype of content2: {type(content2)} \nlength of content2: {len(content2)}')

# * Readline => Read line by line
# with open('file.txt',
#           'r') as file:
#     # First Method
#     print(file.readline())
#     print(file.readline())

# Second method
# with open('file.txt',
#           'r') as file:
#     for x in file:
#         print(x)

# with open('file.txt',
#           'r') as file:
#     text = file.read()
#     print(f'text:\n',
#           text)
#     lines = text.split('\n')
#     print(f'\nlines:\n',
#           lines)

# ! Fourth Example
# text = 'Python BootCamp by TechIstanbul is too good.\n'
# file2 = open('file2.txt',
#              'a')
# file2.write(text)
# file2.close()
#
# with open('file2.txt',
#           'a') as file:
#     file.write('This course held 80 hours')

# ! Fifth Example
# * Deleting files
# import os
#
# if 'file3.txt':
#     os.remove('file3.txt')
#     print('File deleted')
# else:
#     print('File does not exist')

# ! Sixth Example
# with open('shopping_list.txt',
#           'a') as file:
#     while True:
#         item = input('Please add item (to exit Q)? ')
#         if item.lower() == 'q':
#             break
#         else:
#             file.write(item + '\n')

# ! Seventh Example
# import random
#
# with open('game.txt',
#           'w') as file:
#     while True:
#         answer = int(input('Choose your: \n1 for Game \n2 for Statistics \n3 for Exit \n'))
#         if answer == 1:
#             file = open('game.txt',
#                         'a')
#             random_number = random.randrange(1,
#                                              100)
#             file.write(str(random_number) + ', ')
#             guess_number = 10
#             ceil = 0
#             top = 100
#             while guess_number >= 1:
#                 guess = int(input(f'Enter a number {ceil} - {top} '))
#                 file.write(str(guess) + ', ')
#                 if guess == random_number:
#                     file.write(f'{random_number} +  you win')
#                     print('Congratz')
#                     break
#                 elif guess > random_number:
#                     print('Enter number')
#                     top = guess
#                 elif guess < random_number:
#                     print('Enter higher number')
#                     ceil = guess
#                 guess_number -= 1
#                 print(f'You have {guess_number} guesses left')
#                 if guess_number == 0:
#                     file.write(f'{random_number} +  you lose')
#                     print('You lose')
#                     break
#
#         elif answer == 2:
#             with open('game.txt',
#                       'r') as file:
#                 print(file.read())
#         elif answer == 3:
#             print('Exiting the program')
#             break

# ! Eighth Example
# * CSV Files
# with open('students.csv',
#           'w',
#           encoding='utf-8') as file:
#     file.write('Name, Age, Department\n')
#     file.write('John, 22, Computer Eng.\n')
#     file.write('Jane, 45, Chemical Eng.\n')
#     file.write('Jack, 35, Mathematics\n')
#     file.write('Jill, 56, Physics\n')
#
# with open('students.csv',
#           'r',
#           encoding='utf-8') as file:
#     print(file.read())

# ! Ninth Example
# import csv
#
# with open('students.csv',
#           'w',
#           encoding='utf-8',
#           newline='\n') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Name',
#                      'Age',
#                      'Department'])
#     writer.writerow(['John',
#                      22,
#                      'Computer Eng.'])
#     writer.writerow(['Jane',
#                      45,
#                      'Chemical Eng.'])
#     writer.writerow(['Jack',
#                      35,
#                      'Mathematics'])
#     writer.writerow(['Jill',
#                      56,
#                      'Physics'])

# ! Tenth Example
# import csv
#
# with open('students.csv',
#           'r',
#           encoding='utf-8',
#           newline='\n') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

# ! Eleventh Example
# dictionary format
# import csv
#
# with open('students.csv',
#           'r',
#           encoding='utf-8',
#           newline='\n') as file:
# field_names = ['Name',
#                'Age',
#                'Department']

# field_names = file.readline().strip().split(',')  # short way
#
# reader = csv.DictReader(file,
#                         fieldnames=field_names)
# for row in reader:
#     print(row)

# for row in reader:
#     line = row.strip().split(',')
#     student = dict(zip(field_names,
#                        line))
#     print(student)

# ! Twelfth Example
# * Json format
import json

student = {
    'name': 'John',
    'age': 23,
    'department': 'Mathematics',
    }

with open('students.json',
          'w',
          encoding='utf-8') as file:
    json.dump(student,
              file,
              indent=4)

with open('students.json',
          'r') as file:
    data = json.load(file)
    print(data,
          type(data))
    for student in data:
        print(student['age'],
              type(student['age']))

# ! Thirteenth Example
