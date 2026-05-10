"""
Shopping List

"""

amount = int(input("How many vegetables will you buy? "))

vegetables = []
for i in range(1, amount + 1):
    print(i, "What do you want? ")
    vegetable = input("vegetable: ")
    vegetables.append(vegetable)

print(vegetables)

for vegetable in vegetables:
    print(vegetable)
