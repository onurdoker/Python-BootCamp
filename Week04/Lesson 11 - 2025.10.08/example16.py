"""
Python's encapsulation relies on good programming conventions rather than strict rules, complementing manual definition. Access modifiers help you distinguish between the "internal workings" and the "external interface" of your code, enabling more maintainable and organized code.
"""


class Athlete:
  def __init__(self, name, field, gold, silver, bronze):
    self.name = name
    self.field = field
    self.mbronze = bronze  # public data, a variable that is accessible to the public
    self._msilver = silver  # protected data, a variable that is partially hidden
    self.__mgold = gold  # private data, a variable that is complately hidden

  def athlete_info(self):
    return "Athlete name: {}, Field: {}".format(athlete1.name, athlete1.field)

  @property
  def a_print(self):
    gold_medal = self.__mgold
    return "Number of gold medals: {}".format(self.__mgold)


athlete1 = Athlete("Jack", "splinter", 2, 3, 9)
print(athlete1.athlete_info())
# Athlete Name: Jack, Field: splinter

print("Number of bronze medal: ", athlete1.mbronze)
# Number of bronze medal:  9

print("Number of silver medals: ", athlete1._msilver)
# Number of silver medals:  3

# print("Number of gold medals:", athlete1.__mgold)
# Traceback (most recent call last):
#   File "/Users/odoker/Documents/Projects/Python/Python-BootCamp/Week04/Lesson 11 - 2025.10.08/example16.py", line 34, in <module>
#     print("Number of gold medals:", athlete1.__mgold)
# AttributeError: 'Athlete' object has no attribute '__mgold'

print(athlete1.a_print)
# Number of gold medals: 2
