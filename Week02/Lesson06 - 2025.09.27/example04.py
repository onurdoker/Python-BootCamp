"""
FUNCTIONS

without parameters and with return value
"""


def greetings():
    name = input("Please enter your name: ")
    print(f"Welcome {name}")
    return name


print(greetings())

x = greetings()
print(x, type(x))  # Jack <class 'str'>
# Jack
