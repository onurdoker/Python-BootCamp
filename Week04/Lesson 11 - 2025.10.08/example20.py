"""
3. Private Members:

Definition: Begins with a double underscore (__)
Access: This is the most restrictive method on Python.
Members cannot be accessed directly from outside the class.

Purpose: Used to hide the most critical or sensitive data or helper methods of a class from the outside world.

How It Works (Name Mangling)
When Python encounters an attribute or method that starts with a double underscore, it automatically changes its name
This process is called Name Mangling
__secret_date ==> _ClassName__secret_data

This prevent direct access from outside the class and attempting to do so will raise an AttributeError.
"""


class User:
  def __init__(self, name, password):
    self.name = name  # Public
    self.__password = password  # Private

  def __password_check(self):
    # Private method
    return len(self.__password) > 8

  def login(self, entered_password):
    if self.__password_check() and entered_password == self.__password:
      return "Logged In"
    else:
      return "Wrong or invalid Password"


# Access from outside the class
user1 = User("John", "secret123")


# Accessing Public Attributes
print(user1.name)  # John

# Accessing Private Attributes (Raise Error!!)
try:
  print(user1.__password)
except AttributeError as error:
  print(
    f"\n[ERROR] Direct Access Blocked {error} "
  )  # [ERROR] Direct Access Blocked 'User' object has no attribute '__password'

# Accessing via Public Method (Proper Usage)
print(user1.login("secret"))
# Wrong or invalid Password
print(user1.login("secret123"))
# Logged In

# Name Mangling (Forced Access - Should Not Be Done!)
print(
  f"\nAccessing via Name Mangling: {user1._User__password}"
)  # Accessing via Name Mangling: secret123
