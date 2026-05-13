"""Generates a multiplication table using nested list comprehension."""

multiply_table = [[i * j for j in range(1, 11)] for i in range(1, 11)]
print("Multiplication Table:")
for row in multiply_table:
    print(row)
