def changecase(function):
  def myinner():
    return function().upper()

  return myinner


@changecase
def myfunction():
  return "Hello World"


@changecase
def otherfunction():
  return "Python Bootcamps!"


print(myfunction())
print(otherfunction())
# HELLO WORLD
# PYTHON BOOTCAMPS!
