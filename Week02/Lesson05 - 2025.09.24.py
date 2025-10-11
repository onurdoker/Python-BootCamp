# ! First Example
# square = []
# for i in range(1,
#                11):
#     square.append(i ** 2)
# print(square)
#
# numbers = list(range(1,
#                      11))
# print(numbers)
# squares = [i ** 2 for I in numbers]
# print(squares)

# ! Second Example
# even_numbers = []
# # * Classic method
# for i in range(1,
#                21):
#     if i % 2 == 0:
#         even_numbers.append(i)
#
# print(even_numbers)
#
# # * Modern method
# even_numbers = [x for x in range(1,
#                                  21) if x % 2 == 0]
# print(even_numbers)

# ! Third Example
# sentence = 'TechIstanbul Python BootCamp Welcome Good Luck'
# words = sentence.split()
# print(words)
# length = [len(word) for word in words]
#
# for word, length in zip(words,
#                         length):
#     print(word,
#           length)

# ! Fourth Example
# person = ('Onur',
#           'Doker',
#           48)
#
# name, surname, age = person
# print(name,
#       surname,
#       age)

# ! Fifth Example
# Dictionary
# student = ['Ali',
#            22,
#            'Computer Engineering',
#            85]
#
# student_dict = {'name': 'Ali',
#                 'age': 22,
#                 'department': 'Computer Engineering',
#                 'grade': 85}
#
# vehicle = {'brand': 'Toyota',
#            'model': 'Corolla',
#            'year': 2020,
#            'color': 'red'}

# print(vehicle)
# print(type(vehicle))
# print(vehicle['brand'])
#
# del vehicle['color']
# print(vehicle)
#
# vehicle['range'] = 9000
# print(vehicle)

# print(vehicle.keys())
# print(vehicle.values())
# print(vehicle.items())

# for dd in vehicle:
#     print(dd,
#           vehicle[dd])

# for key, value in vehicle.items():
#     print(key,
#           value)

# student = {
#     'name': 'Timur',
#     'age': 57,
#     'department': 'Computer Engineering',
#     }
#
# print(student,
#       type(student))
# print(student['name'])
# print(student.get('age'))
# print(student['surname'])
# print(student.get('surname'))

# ! Sixth Example
# products = [
#     {'name': "laptop", 'price': 25000, "stock": 30},
#     {'name': "mause", 'price': 250, "stock": 450},
#     {'name': "keyboard", 'price': 41, "stock": 39},
#     ]
#
# for product in products:
#     print(product)
#     print(f"{product['name']} - {product['price']} - {product['stock']}")

# ! Seventh Example
# eng_tr = {'car': 'araba', 'pencil': 'kalem', 'red': 'kırmızı'}
# print(eng_tr)
#
# for key, value in zip(eng_tr.keys(),
#                       eng_tr.values()):
#     print(key,
#           '=>',
#           value)

# ! Eighth Example
# * First answer
# students = []
#
# print('=' * 5,
#       'Student Score System',
#       '=' * 5)
# print('To Exit press Q')
#
# while True:
#     name = input('Enter student name: ')
#     if name.upper() == 'Q':
#         break
#     else:
#         score = int(input('Enter student score: '))
#         students.append({'name': name, 'score': score})
# print(students)

# * Second answer
# students = []
# while True:
#     name = input('Enter student name: ')
#     if name.upper() == 'Q':
#         break
#     surname = input('Enter student surname: ')
#     if surname.upper() == 'Q':
#         break
#     number = int(input('Enter student number: '))
#     if number < 0 or number > 100:
#         break
#     students.append({'name': name, 'surname': surname, 'number': number})
#
# print(students)

# ! Ninth Example
# products = []
# print('to exit press Quit')
# while True:
#     name = input('Enter product name: ')
#     if name.lower() == 'quit':
#         break
#     else:
#         price = float(input('Enter product price: '))
#         stock = int(input('Enter product stock: '))
#         products.append({'name': name,
#                          'price': price,
#                          'stock': stock})
# print(products)

# ! Tenth Example
menu = []
# foods = {
#     "Soups": ["with meat",
#               "with legumes",
#               "with vegetables"],
#     "Kebaps": ["spicy",
#                "w/o spices",
#                "durums"],
#     "Drinks": ["Tea",
#                "Coffee"],
#     }

# print(foods)
#
# for category in foods:
#     print(category)
#     for food in foods[category]:
#         print("\t",
#               food)

# foods = {
#     "Soups": {
#         "with meat": ["iskembe",
#                       "kelle paca"],
#         "with legumes": ["mercimek",
#                          "ezogelin"],
#         "with vegetables": ["mantar",
#                             "brokoli"],
#         },
#     "Kebaps": {"spicy": ["Adana",
#                          "Mardin"],
#                "w/o spices": ["urfa",
#                               "antep"],
#                "durums": ["adana durum",
#                           "urfa durum"]},
#     "Drinks": ["Tea",
#                "Coffee"],
#     }
#
# for main_category in foods:
#     print(main_category)
#     if type(foods[main_category]) is dict:
#         for category in foods[main_category]:
#             print('\t',
#                   category)
#             if type(foods[main_category][category]) is dict:
#                 for subcategory in foods[main_category][category]:
#                     print('\t\t',
#                           subcategory)
#                     for subcategory2 in foods[main_category][category][subcategory]:
#                         print('\t\t\t',
#                               subcategory2)
#             else:
#                 print('\t\t',
#                       foods[main_category][category])
#     else:
#         print('\t',
#               foods[main_category])

# ! Eleventh Example
# players = {
#     'BJK': ["Rafa",
#             "Cengiz",
#             'Salih'],
#     'FB': ['Fred',
#            'Asensio',
#            'Talisca'],
#     'GS': ['Oshimen',
#            'Sane',
#            'Icardi'],
#     }
#
# print(players["FB"])
#
# # * first method
# for team in players:
#     print(team)
#     print(players[team])
#
# # * Second method
# for team in players:
#     print(team)
#     for player in players[team]:
#         print('\t',
#               player)

# ! Twelfth Example
# week_in = {"Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5}
# week_end = {"Saturday": 6, "Sunday": 7}
#
# week_days = {}
# week_days.update(week_in)
# week_days.update(week_end)
# print(week_days)
#
# print(len(week_in))
#
# day = 'Sunday'
#
# if day in week_days:
#     print('day added')

# ! Thirteenth Example
# items = {}
#
# print("enter your items and prices")
# print("to exit press Q")
# while True:
#     name = input('Enter item name: ')
#     if name.upper() == 'Q':
#         break
#     else:
#         price = float(input('Enter item price: '))
#     items[name] = price
# print(items)
# total_price = sum(items.values())

# ! Fourteenth Example
# numbers = [1,
#            2,
#            3,
#            4,
#            6]
# square = {x: x ** 2 for x in numbers}
# print(square)

# ! Fifteenth Example
# numbers = list(range(1,
#                      11))
# # numbers = [x for x in range(1,11)]
# even_numbers = {x: x * 2 for x in numbers if x % 2 == 0}
# print(even_numbers)

# ! Sixteenth Example
school = {
    "9A": [
        {'name': 'Ali', 'number': '101'},
        {'name': 'Ayse', 'number': '102'},
        ],
    '10B': [
        {'name': 'Mehmet', 'number': '201'},
        {'name': 'Zeynep', 'number': '202'},
        ],
    }

for class_, students in school.items():
    print(f'\n{class_}')
    for student in students:
        print(f' - {student["name"]} (Number: {student["number"]})')
