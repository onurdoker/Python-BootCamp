"""
List functions
"""

fruits = ["apple", "pineapple", "strawberry", "peach", "banana", "orange"]

print(fruits)
# ["apple", "pineapple", "strawberry", "peach", "banana", "orange"]


print(fruits.count("strawberry"))  # 1
print(fruits.index("pineapple"))  # 1

fruits.append("lemon")
print(fruits)
# ['apple', 'pineapple', 'strawberry', 'peach', 'banana', 'orange', 'lemon']

fruits.insert(0, "banana")
print(fruits)
#  ['banana', 'apple', 'pineapple', 'strawberry', 'peach', 'banana', 'orange', 'lemon']

fruits[1] = "mandarin"
print(fruits)
# ['banana', 'mandarin', 'pineapple', 'strawberry', 'peach', 'banana', 'orange', 'lemon']

fruits.sort()
print(fruits)
# ['banana', 'banana', 'lemon', 'mandarin', 'orange', 'peach', 'pineapple', 'strawberry']

fruits.reverse()
print(fruits)
# ['strawberry', 'pineapple', 'peach', 'orange', 'mandarin', 'lemon', 'banana', 'banana']

new_fruits = ["fig", "grape"]
fruits.extend(new_fruits)
print(fruits)
# ['strawberry', 'pineapple', 'peach', 'orange', 'mandarin', 'lemon', 'banana', 'banana', 'fig', 'grape']

new_fruits2 = ["watermelon", "mango"]
fruits.append(new_fruits2)
print(fruits)
#  ['strawberry', 'pineapple', 'peach', 'orange', 'mandarin', 'lemon', 'banana', 'banana', 'fig', 'grape', ['watermelon', 'mango']]

fruits.pop()
print(fruits)
# ['strawberry', 'pineapple', 'peach', 'orange', 'mandarin', 'lemon', 'banana', 'banana', 'fig', 'grape']

fruits.pop(3)
print(fruits)
# ['strawberry', 'pineapple', 'peach', 'mandarin', 'lemon', 'banana', 'banana', 'fig', 'grape']

fruits.remove("pineapple")
print(fruits)
# ['strawberry', 'peach', 'mandarin', 'lemon', 'banana', 'banana', 'fig', 'grape']

del fruits[1]
print(fruits)
# ['strawberry', 'mandarin', 'lemon', 'banana', 'banana', 'fig', 'grape']

fruits.clear()
print(fruits)
# []

del fruits
print(fruits)  # Error -> name 'fruits' is not defined
