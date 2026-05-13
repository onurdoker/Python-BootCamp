def greetings(name, message="welcome to the Python Bootcamp!"):
    print(f"Hello {name} {message}")


# greetings()  # Error: missing required argument 'name'

greetings("John")  # Hello John welcome to Python Bootcamp!
greetings("Jill", "have a nice day")  # Hello Jill have a nice day
