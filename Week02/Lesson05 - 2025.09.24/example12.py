"""
Take numbers from a list, calculate their squares and create a dictionary containing the original number and its square.
"""

# Classical method
numbers = [1, 2, 3, 4, 5, 6]
num_dict = {}

for number in numbers:
    num_dict[number] = number**2

print(num_dict)

# Modern method (by list comprehension)
numbers = [1, 2, 3, 4, 5, 6]
num_dict2 = {number: number**2 for number in numbers}
print(num_dict2)
