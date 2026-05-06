"""
input() take data from user
"""

name = input("Enter your name: ")  # Enter your name:
print("Nice to meet you, ", name)


print("How old are you?")
age = input()  # input always takes data as string
print(type(age))  # <class 'str'>
age = int(age)
print(type(age))  # <class 'int'>
print(age * 2)
