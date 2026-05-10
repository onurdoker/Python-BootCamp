"""
Working on Categoric Data Types
"""

vegetables = ["potato", "onion"]
fruits = ["apple", "fig"]
food = ["cheese", "honey"]
greenlet = ["parsley", "arugula", "purslane"]

# When combining different lists, simply concatenating them is not always desirable, especially when working with categorical data.
shopping_list = vegetables + fruits + food + greenlet

print(shopping_list)
# ['potato', 'onion', 'apple', 'fig', 'cheese', 'honey', 'parsley', 'arugula', 'purslane']

print(len(shopping_list))  # 9
print(shopping_list[0])  # potato
print(shopping_list[0][1])  # o


# If we structure the arrangement as list within a list, it allows for more complex data structure
shopping_list2 = [vegetables, fruits, food, greenlet]
print(shopping_list2)
# [['potato', 'onion'], ['apple', 'fig'], ['cheese', 'honey'], ['parsley', 'arugula', 'purslane']]

print(len(shopping_list2))  # 4
print(shopping_list2[0])  # ["potato", "onion"]
print(shopping_list2[0][1])  # onion

for category in shopping_list2:
    print(category)
    for item in category:
        print("\t", item)


# If we want to add new elements to a list;
shopping_list2.append("cheesecake")

print(shopping_list2)
# [['potato', 'onion'], ['apple', 'fig'], ['cheese', 'honey'], ['parsley', 'arugula', 'purslane'], 'cheesecake']

# When dealing nested lists, we need to consider the context of categories or lists while performing operations like adding elements or manipulating the list structure.

for category in shopping_list2:
    print(category)
    if type(category) != list:
        continue
    for item in category:
        print("\t", item)
