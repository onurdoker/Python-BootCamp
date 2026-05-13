"""
FUNCTIONS

without parameters and not return value
"""


def greetings():
    print("Hello Python Bootcamp Program")
    print("This Bootcamp was organized by TechIstanbul and Ecodation")


greetings()
greetings()
greetings()

print(greetings, type(greetings))
# <function greetings at 0x11d2ddc60> <class 'function'>

a = greetings()
print(a, type(a))
# None <class 'NoneType'>
