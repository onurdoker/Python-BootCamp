"""
Multi Inheritance in Python

Python supports multiple inheritance. Multiple inheritance means that a class can inherit from more than one parent class.

Syntax:
class Base1:
    body of the base class

class Base2:
    body of the base class

class Derived(Base1, Base2):
    body of the derived class

"""


class Football_Player:
  running = "Can run"
  sprint = "Can sprint"
  salary = 500

  def __init__(self, foot="right"):
    self.foot = foot
    self.spot = "mid-field"

  def spirit(self):
    print("Accelerated 20 units")


class Basketball_Player:
  vault = "Can vault"
  three_point_shot = "Can three-point shot"
  salary = 750

  def __init__(self):
    self.spot = "Offence"

  def spirit(self):
    print("Accelerated 20 units")


class Multi_Player(Football_Player, Basketball_Player):
  def __init__(self, foot):
    Basketball_Player.__init__(self)
    Football_Player.__init__(self, foot)


Jack = Multi_Player("left")
print("Vault: ", Jack.vault)  # Vault:  Can vault
print("Is Jack runnable: ", Jack.running)  # Is Jack runnable:  Can run
print("Jack's Salary is: ", Jack.salary)  # Jack's Salary is:  500

Jack.spirit()  # Accelerated 20 units
