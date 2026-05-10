"""
TUPLES

Tuples (ordered, unchangeable, and allow duplicate values)
Tuples are contain multiple items like strings, numbers, boolean values, other lists, other tuples, etc.

tuple1 = ( #1 , #2 )
tuple1 = #1, #2
"""

personal1 = "John", "Jane"  # or personal1 = ('John', 'Jane')
print(personal1, type(personal1))  # ('John', 'Jane') <class 'tuple'>

personal2 = ("Jack",)
print(personal2, type(personal2))  # ('Jack',) <class 'tuple'>

string2 = "Jill"
print(string2, type(string2))  # Jill <class 'str'>

print(personal2.count("Jack"))  # 1

print("Jill" in personal2)  # False
