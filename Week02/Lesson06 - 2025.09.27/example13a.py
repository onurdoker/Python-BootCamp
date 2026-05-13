"""
Use default values in variable declarations and function parameters
"""


def greetings(name="Guess"):
    print(f"Hello {name} welcome to the Python Bootcamp!")


greetings()  # Hello Guess welcome to the Python Bootcamp!
greetings("John")  # Hello John welcome to Python Bootcamp!
