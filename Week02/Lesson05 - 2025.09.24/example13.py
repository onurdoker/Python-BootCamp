"""
Create a dictionary containing even numbers from 1 to 10 squared
"""

# Classical method
# all code same
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers = list(range(1, 11))
numbers = [x for x in range(1, 11)]

desired_dict = {}
for number in numbers:
    if number % 2 == 0:
        desired_dict[number] = number**2

print(desired_dict)

# Modern method (by list comprehension)
numbers = list(range(1, 11))
desired_dict2 = {number: number**2 for number in numbers if number % 2 == 0}
print(desired_dict2)
