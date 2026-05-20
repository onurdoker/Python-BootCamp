"""
What is a Decorator?

- A decorator is a Python function that wraps around function, altering its behaviour.

- It adds or modifies a special attribute to a function, either before or after it.
"""

# without decorator
# def greetings():
#   print('Hello')

# greetings()


# with decorator
def decorator(func):
  def wrapper():
    print("Before function execution")
    func()
    print("After function execution")

  return wrapper


@decorator
def greetings():
  print("Hello")


greetings()
