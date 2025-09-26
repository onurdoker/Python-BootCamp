# ! First Example
# * Collections
# * Lists
# * Lists (ordered, changeable, and allow duplicate values)
# name1 = "onur"
# name2 = "timur"
# name3 = "enes"
# students = [name1,
#             name2,
#             name3]
#
# print(students,
#       type(students))

# * Lists are contain multiple items like strings, numbers, boolean values, other lists, etc.
# student_name = "John"
# student_surname = "Doe"
# student_number = 153
# student_attend = True
# student_average = 3.60
#
# student1 = [student_name,
#             student_surname,
#             student_number,
#             student_attend,
#             student_average]
# print(student1,
#       type(student1))
#
# student2 = ["Jane",
#             "Cane",
#             140,
#             True,
#             2.87]
# print(student2,
#       type(student2))
#
# print(student2[2])
# print('Length of student1:',
#       len(student1))
# print('Length of student2:',
#       len(student2))
#
# print("ali" in student2)
#
# for student_knowledge in student1:
#     print(student_knowledge)
#
# for i in range(len(student2)):
#     print(student2[i])

# ! Second Example
# name = "onur"
# letter_of_name = list(name)
# print(letter_of_name)
# print(type(letter_of_name))
#
# new_string = str(letter_of_name)
# print(new_string,
#       type(new_string))
# print(len(new_string))
# for letter in new_string:
#     print(letter)

# ! Third Example
# fruits = ["banana",
#           "apricot",
#           "orange"]
# print(fruits)
# fruits.append("apple")
#
# print(fruits[0])
# print(fruits.index('banana'))
# print(fruits.count('banana'))
#
# fruits.insert(1,
#               'apple')
# print(fruits)
#
# fruits[1] = 'peach'
# print(fruits)
#
# fruits.sort()
# print(fruits)
#
# fruits.reverse()
# print(fruits)
#
# fruits1 = ['mango',
#            'grapes']
# fruits.extend(fruits1)
# print(fruits)
#
# fruits2 = ["cherry",
#            'blueberry']
# fruits.append(fruits2)
# print(fruits)
#
# fruits.pop()
# print(fruits)
#
# fruits.pop(2)
# print(fruits)

# fruits.remove("banana")
# print(fruits)
#
# del fruits[2]
# print(fruits)
#
# fruits.clear()
# print(fruits)
#
# del fruits
# print(fruits)

# ! Fourth Example
# piece = int(input('How many vegetables will you buy? '))
#
# vegetables = []
# for i in range(1,
#                piece + 1):
#     print(i,
#           'What do you want')
#     vegetable = input('vegetable: ')
#     vegetables.append(vegetable)
#
# print(vegetables)
#
# for vegetable in vegetables:
#     print(vegetable)

# message = "Welcome to shopping list program \n for exit program press x"
# print(message)
# vegetables = []
# while True:
#     vegetable = input('What do you want: ')
#     if vegetable.lower() == 'x':
#         print("shopping list: ",
#               vegetables)
#         break
#     elif vegetable == "":
#         continue
#     else:
#         vegetables.append(vegetable)

# ! Fifth example
# vegetables = ['tomato',
#               'onion']
#
# fruits = ['apple',
#           'pear']
#
# foods = ['cheese',
#          'honey']
#
# greenlet = ['parsley',
#             'arugula',
#             'purslane']

# shopping_list = vegetables + fruits + foods + greenlet
# print(shopping_list)

# shopping_list = [vegetables,
#                  fruits,
#                  foods,
#                  greenlet]
# print(shopping_list)
# print(shopping_list[0])
# print(shopping_list[0][1])  # onion
# print(shopping_list[3][2])  # purslane

# for category in shopping_list:
#     print(category)
#     for item in category:
#         print('\t',
#               item)

# shopping_list.append('cheesecake')
#
# for category in shopping_list:
#     print(category)
#     if category != list:
#         continue
#     for item in category:
#         print('\t',
#               item)

# ! Sixth Example
# * Tuples
# * Tuples (ordered, unchangeable, and allow duplicate values)
# * Tuples are contain multiple items like strings, numbers, boolean values, other lists, other tuples, etc.

# person1 = 'onur', 'doker'
# print(person1,
#       type(person1))
#
# # if only contain one item, person1 = ('onur',)
# person2 = ('john',)
# print(person2,
#       type(person2))
#
# person3 = ('john')
# print(person3,
#       type(person3))
#
# print(person2.count('onur'))
# print('onur' in person2)

# ! Seventh Example
# tuple_ = (24,
#           8,
#           2.5,
#           'Mert',
#           True,
#           'Mert',
#           ['Mert',
#            'Can',
#            'John'],
#           (24,
#            8,
#            2.5,
#            True,
#            'Mert',
#            []))
# print(tuple_)
# print(type(tuple_))
#
# list = ['apple',
#         'pear']
# list_tuple = tuple(list)
# print(list_tuple,
#       type(list_tuple))
#
# print(tuple_.index('Mert'))
# print(tuple_.count('Mert'))
#
# for item in tuple_:
#     print(item)
#
# print(tuple_[:3])
# print(tuple_[::-1])

# ! Eighth Example
# * Sets
# * Sets (unordered, unchangeable, and unindexed)
# * Sets are contain multiple items like strings, numbers, boolean values, other lists, other tuples, etc.
# students = {'Ali', 'Veli', 'Can', 'Canan', 'Onur'}
# print(students,
#       type(students),
#       len(students))
#
# students2 = {'Ali', 'Veli', 'Can', 'Canan', 'Onur', 'Can'}
# print(students2,
#       type(students2),
#       len(students2))

# students.pop()
# print(students)
#
# for student in students:
#     print(student)
#
# print('John' in students)

# ! Ninth Example
# group1 = {'a', 'b', 'c'}
# group2 = {1, 2, 3}
#
# combine_group1 = group1 | group2
# print(combine_group1)
#
# combine_group2 = group1.union(group2)
# print(combine_group2)

# ! Tenth Example
# print('Note books')
# print('To exit write quit')
# notes = []
# while True:
#     new_note = input('Enter your note: ')
#     if new_note.lower() == 'quit':
#         break
#     notes.append(new_note)
# print('Your Notes: ')
# for note in notes:
#     print('-',
#           note)

# ! Eleventh Example
# number = 5
# guess = int(input('Enter your guess (1 to 10): '))
# while True:
#     if guess <= 0 or guess >= 11:
#         print('You have to enter a number between 1 and 10')
#         pass
#     elif guess == number:
#         print('Congratulations!, you find correct number')
#         break
#     elif guess < number:
#         print('Too low')
#     else:
#         print('Too high')
#     guess = int(input('Enter your new guess (1 to 10): '))


#
girls = ['liz',
         'fatma',
         'hayriye']
boys = ['ali',
        'veli',
        'can']
list1 = [girls,
         boys]

for dd in list1:
    for person in dd:
        print(dd,
              person)

for girl, boy in zip(girls,
                     boys):
    print(girl,
          boy)
