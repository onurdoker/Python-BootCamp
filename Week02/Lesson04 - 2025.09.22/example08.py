"""
Tuples can hold different types of data
"""

tuple_ = (
    24,
    8,
    2.5,
    "Jack",
    True,
    "Jack",
    ["Jack", "John", "Jim"],
    (24, 8, 2.5, "Jack"),
    [],
)

print(tuple_)
# (24, 8, 2.5, 'Jack', True, 'Jack', ['Jack', 'John', 'Jim'], (24, 8, 2.5, 'Jack'), [])

print(type(tuple_))  # <class 'tuple'>

list_ = ["apple", "pear"]
tuple_list = tuple(list_)
print(tuple_list)  # ('apple', 'pear')

print(tuple_.index("Jack"))  # 3 (first occurrence of Jack)
print(tuple_.count("Jack"))  # 2 (number of times Jack appears in the tuple)

for dd in tuple_:
    print(dd)

print(tuple_[:3])  # (24, 8, 2.5)
print(
    tuple_[::-1]
)  # ([], (24, 8, 2.5, 'Jack'), ['Jack', 'John', 'Jim'], 'Jack', True, 'Jack', 2.5, 8, 24)
print(tuple_[6][1])  # John
