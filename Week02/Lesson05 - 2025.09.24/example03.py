"""
DICTIONARY
"""

# Example1

student = ["John", 22, "Computer Engineer", 85]

student_dict = {
    "name": "John",
    "age": 22,
    "department": "Computer Engineering",
    "grade": 85,
}

# Example2
car = {"brand": "Toyota", "model": "Corolla", "year": 2020, "color": "Grey"}

print(car)  # {'brand': 'Toyota', 'model': 'Corolla', 'year': 2020, 'color': 'Grey'}
print(type(car))  # <class 'dict'>

print(car["brand"])  # Toyota
print(car["year"])

car["year"] = 2022
print(car)  # {'brand': 'Toyota', 'model': 'Corolla', 'year': 2022, 'color': 'Grey'}

del car["color"]
print(car)  # {'brand': 'Toyota', 'model': 'Corolla', 'year': 2020}

car["range"] = 9000
print(car)  # {'brand': 'Toyota', 'model': 'Corolla', 'year': 2022, 'range': 9000}

"""
Dictionaries have key and value pairs.
Keys are unique and immutable ( strings, numbers, tuples).
Keys can be added or removed from a dictionary.
Keys can also be updated in a dictionary.
Keys can be used to check if a key exists in a dictionary.
Keys can be used to sort/filter/group data in a dictionary.
Keys can be used to create/update/delete a dictionary from an existing dictionary.

Values can be of any data type.
Values are accessed using keys.
"""
print(car.keys())
# dict_keys(["brand", "model", "year", "range"])

print(car.values())
# dict_values(["Toyota", "Corolla", 2022, 9000])

for key in car:
    print(key, car[key])
# brand Toyota
# model Corolla
# year 2022
# range 9000

print(car.items())
# dict_items([('brand', 'Toyota'), ('model', 'Corolla'), ('year', 2022), ('range', 9000)])

for key, value in car.items():
    print(key, value)
# brand Toyota
# model Corolla
# year 2022
# range 9000
