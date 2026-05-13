def greetings(name):
    print(f"Hello {name}, \nWelcome to Python Bootcamp Program")
    if len(name) < 5:
        return True
    else:
        return False


name = input("Please enter your name: ")
answer = greetings(name)
if answer:
    print("Your name is too short")
else:
    print("Your name is valid")
