"""
List Comprehension Exercises

You can create a list in a single line using a for loop or conditional statements, depending on your requirements.
"""

# Classical method
squares = []
for i in range(1, 11):
    squares.append(i**2)

print(squares)

# Modern method (by list comprehension)
numbers = list(range(1, 11))
print(numbers)

squares2 = [x**2 for x in numbers]
print(squares2)
