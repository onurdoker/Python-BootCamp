"""
Create a list even numbers between 1 and 20
"""

# Classical method
even_numbers = []
for dd in range(1, 21):
    if dd % 2 == 0:
        even_numbers.append(dd)

print(even_numbers)

# Modern method (by list comprehension)
even_numbers2 = [dd for dd in range(1, 21) if dd % 2 == 0]
print("Even numbers: ", even_numbers2)
