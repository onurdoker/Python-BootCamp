"""
Logical Operators

When we have logical data types or operations that involve logical data, we use logical operators to perform operations on them.

We have 3 logical operators in Python:
- and: Returns True if both operands are True.
- or: Returns True if at least one operand is True.
- not: Returns the opposite of the given operand (True becomes False and vice versa).
"""

print((20 >= 18) and (0 >= 1))  # True and False => False
print((20 >= 18) and (3 >= 1))  # True and True => True

print((20 >= 18) or (0 >= 1))  # True or False => True
print((15 >= 18) or (0 >= 1))  # False or False => False

print(not (False))  # True
