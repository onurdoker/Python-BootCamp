# import example08
from example08 import greetings

name = input("Please enter your name: ")

# answer = example08.greetings(name)
answer = greetings(name)
if answer:
    print("Your name is too short")
else:
    print("Your name is valid")
