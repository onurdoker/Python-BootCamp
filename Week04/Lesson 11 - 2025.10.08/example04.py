def changecase(n):
  def changecase(function):
    def myinner():
      if n == 1:
        a = function().lower()
      else:
        a = function().upper()
      return a

    return myinner

  return changecase


@changecase(2)
def myfunction():
  return "Hello Linus!"


print(myfunction())
