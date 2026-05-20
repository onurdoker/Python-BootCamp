"""
Using multiple decorators to enhance a function.

"""


def first_decorator(greeting):
  def wrapper():
    print("First decanter started")
    greeting()

  return wrapper


def second_decorator(greeting):
  def wrapper():
    print("Second decanter started")
    greeting()

  return wrapper


@first_decorator
@second_decorator
def greeting():
  print("Hello, world!")


greeting()
