# ! First Example
# name = 'Buray'
# if name == 'Burak':
#     print ('we have same name')

# if name != 'Burak':
#     print ('we do not have same name')

# name2 = input('What is your name? ')
# if name2 == name:
#     print ('we have same name')
# else:
#     print ('we do not have same name')


# ! Second Example
# ans = int(input('Did you attend course? (1/0) '))
# answer = bool(ans)
#
# print('Attendance statues ',
#       answer)
# if answer:
#     print('You attended the course')


# ! Third Example
# name = input('What is your name? ')
#
# if name == 'emir' or name == 'burak':
#     print('we have same name', name)

# if not(name == 'emir' or name == 'burak'):
#     print('we have not same name', name)

# ! Fourth Example
# name = 'semanur2'

# if name == 'semanur':
#     print('we have same name')
#     print('Nice to meet you')
# else:
#     print('we do not have same name')


# ! Fifth Example
# birth_year = int(input('Enter your birth year: '))
# age = 2025 - birth_year
#
# if age >= 18:
#     print('You are not eligible to vote')
# else:
#     print('You can not get driver license')
#     print(f'You are {age} years old')
#     print(f'You have to wait {18 - age} years to get driver license')


# ! Sixth Example
# road = float(input('Enter the road length (km): '))
# time = float(input('Enter the time (h): '))
# speed = road / time
#
# if speed > 132:
#     print(f'Your speed is {speed} km/h')
#     print('You are speeding')
# else:
#     print(f'Your speed is {speed} km/h')
#     print('Thanks for driving safely')

# ! Seventh Example
# food = input('enter food name: ')
# drink = input('enter drink name: ')
#
# if food == 'pizza' and drink == 'cola':
#     print('Valid order')
# else:
#     print(f'{food} - {drink} is not valid order')
#
# food = input('enter food name: ')
# drink = input('enter drink name: ')
#
# if food == 'pizza':
#     print('Pizza valid food order')
#     if drink == 'cola' or drink == 'fanta':
#         print('Valid order')
#         print('Bon Appétit')
#     else:
#         print('Invalid drink order')
# else:
#     print(f'{food} - {drink} is not valid order')
#

# ! Eighth Example
# score = int(input('Enter your score: '))
# if score < 0:
#     print('Invalid score')
# else:
#     if score < 70:
#         print('You cant pass the exam')
#     else:
#         if score < 85:
#             print('You passed the exam')
#         else:
#             if score <= 100:
#                 print('You passed the exam with distinction')
#             else:
#                 print('Invalid score')

# ! Nineth Example
# score = int(input('Enter your score: '))
# if score < 0 or score > 100:
#     print('Invalid score')
# elif score < 70:
#     print('You cant pass the exam')
# elif score < 85:
#     print('You passed the exam')
# elif score <= 100:
#     print('You passed the exam with distinction')

# ! Tenth Example
# classroom = int(input('Enter your class: '))

# if classroom == 0:
#     print('kindergarten')
# elif 1 <= classroom <= 4:
#     print('elementary school')
# elif 5 <= classroom <= 8:
#     print('middle school')
# elif 9 <= classroom <= 12:
#     print('high school')
# else:
#     print('Invalid class')

# ! Eleventh Example
# a = 5
# b = 6
# c = 85

# a, b, c = 5, 6, 85

# print(a + b + c)
# print(a - b - c)

# ! Twelfth Example
# a, b = 9, 15

# print(a, b)

# number1 = a
# number2 = b

# a = number2
# b = number1
# print(a, b)

# a, b = b, a # Short way
# print(a, b)

# ! Thirteenth Example
# a = 2
# if a <= 4:
#     answer = 'less'
# else:
#     answer = 'greater'
# print(answer)

# answer2 = 'less' if a <= 4 else 'greater'  # Short way
# print(answer2)

# ! Fourteenth Example
# day = input('Which day of week is it? ')
#
# if day == '1':
#     print('Monday')
# elif day == '2':
#     print('Tuesday')
# elif day == '3':
#     print('Wednesday')
# elif day == '4':
#     print('Thursday')
# elif day == '5':
#     print('Friday')
# elif day == '6':
#     print('Saturday')
# elif day == '7':
#     print('Sunday')
# else:
#     print('Invalid day')

# ! Fifteenth Example
# day = int(input('Which day of week is it? '))
#
# if day == 1 or day == 3 or day == 6:
#     print('It is Python BootCamp day')
# elif day == 2 or day == 4 or day == 5 or day == 7:
#     print('It is not Python BootCamp day')
# else:
#     print('Invalid day')

# ! Sixteenth Example
# day = int(input('Which day of week is it? '))
#
# match day:
#     case 1:
#         print('Monday')
#     case 2:
#         print('Tuesday')
#     case 3:
#         print('Wednesday')
#     case 4:
#         print('Thursday')
#     case 5:
#         print('Friday')
#     case 6:
#         print('Saturday')
#     case 7:
#         print('Sunday')
#     case _:
#         print('Invalid day')

# ! Seventeenth Example
# day = int(input('Which day of week is it? '))
#
# match day:
#     case 1 | 3 | 5:
#         print('It is Python BootCamp day')
#     case 2 | 4 | 6 | 7:
#         print('It is not Python BootCamp day')
#     case _:
#         print('Invalid day')

# ! Eighteenth Example
# name = 'RidvanCelikbas'
# length = len(name)
# print(length)
# print(name[0])  # first letter
# print(name[13])  # last letter
# print(name[-1])  # last letter
# print(name[1:4])  # 1 to 4
# print(name[:6])  # 0 to 6
# print(name[:6:1])  # 0 to 6 step 1
# print(name[:6:2])  # 0 to 6 step 2
# print(name[-10:-3])  # -10 to -3
# print(name[5::2])  # 5 to end step 2
# print(name[::-1])  # reverse
#
# print('R' in name)  # is 'R' in name? => True
# print('r' in name)  # is 'r' in name? => False (case-sensitive)
#
# print(name.upper())  # to upper case
# print(name.lower())  # to lower case
#
# print(name.isalnum())  # is name alphanumeric?
# print(name.isdigit())  # is name digit?

# ! Nineteenth Example
# name1 = 'Gamze'
# name2 = 'Omer'
# name3 = 'Yasin'

# print(name1 + name2 + name3)
# print(f'{name1} {name2} {name3}')

# text = "Hi Dear {} \nWelcome to Python Bootcamp Program"
# print(text.format(name1))
# print(text.format(name2))
# print(text.format(name3))

# text2 = 'The first, the second and the third place winners of our competition are {}, {} and {}.'
# print(text2.format(name1, name2, name3))
# print(text2.format(name2, name3, name1))
#
# print(text2.count('a'))

# ! Twentieth Example
# print('Omer', 'Yasin', 'Gamze')  # default separator is space

# print('Omer', 'Yasin', 'Gamze', sep=', ')  # separator is comma

# print('Omer', 'Yasin', 'Gamze', sep=' / ')  # separator is slashed

# ! Twenty-First Example
# import random

# random_number = random.randint(1, 10)
# number = int(input("Enter the number you guessed: "))

# if number == random_number:
#     print(f"Congratulations! \nGuessed number is {random_number} ")
# else:
#     print("You did not guess the number \ntry again")
