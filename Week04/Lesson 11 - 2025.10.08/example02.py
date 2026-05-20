import datetime
import time


def log(function):
  def wrapper():
    print("Log: calling function...")
    print(datetime.datetime.now())
    function()
    print("Log: function called.")
    print(datetime.datetime.now())

  return wrapper


@log
def greetings():
  print("Hello, world!")
  time.sleep(5)


greetings()
