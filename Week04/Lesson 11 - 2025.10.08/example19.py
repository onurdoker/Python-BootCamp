"""
2. Protected Conventions

Definition: Begins with underscore (_)
Access: Technically, it is still accessible from anywhere - but this servers as a warning that it's meant for internal of subclass use.
Purpose: Indicates that the member belongs to the internal workings of the class. Its designed to be used by subclasses, but should not be modified directly from outside.

Important Note: Python does not enforce this restriction.
It's the developer's responsibility to respect this convention.

Example:
In a bank account, the balance should only be modified through methods like deposit() or withdraw(), not directly from outside
"""


class BankAccount:
  def __init__(self, account_number, balance=0):
    self.account_number = account_number
    # Protected conversation: Please do not access from the outside
    self._balance = balance

  def deposit(self, amount):
    self._balance += amount
    print(f"The new balance is: ${self._balance}")

  def deposite(self, amount):
    self._balance -= amount
    print(f"The new balance is: ${self._balance}")

  def log(self, transaction):
    print(f"The {self.account_number} logged {transaction}")


# Access from outside the class
account = BankAccount("123456", 1000)

# Proper usage (changing balance via public method)
account.deposit(100)
# The new balance is: $1100

# Technically possible, but improper usage (rule violation)
# Python won't stop you, but this is considered bad programming practice
account._balance = 999
print(f"The account balance is: ${account._balance}")
# The account balance is: $999

# Accessing protected method from outside the class
account.log("Deposit of $100")
# The 123456 logged Deposit of $100
