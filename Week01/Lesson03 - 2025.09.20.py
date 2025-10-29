#! First Example
# for dd in range(10):  # 0 - 9
#     print(dd,
#           'Welcome to Python Bootcamp Program')

# ! Second Example
# * For loops
# print(range(10))
# print(list(range(10)))

# for dd in range(4):  # => 0 - 3
#     print(dd,
#           '. slice of pizza')
# for dd in range(1,
#                 5):  # =>
#     print(dd,
#           '. slice of pizza')
# for dd in range(3,
#                 10,
#                 2):  # =>
#     print(dd,
#           '. slice of pizza')

# for letter in 'Python':  # => P y t h o n
#     print(letter)

# ! Third Example
# name = input('Enter your name: ')
# age = int(input('Enter your age: '))

# for dd in range(age):
#     print(name)

# for dd in range(age):
#     print('{} times {}'.format(dd + 1,
#                                name))

# for dd in range(len(name)):
#     print('{} - {} - {} '.format(dd + 1,
#                                  name,
#                                  name[dd]))

# ! Fourth Example
# start = int(input('Enter start number: '))
# end = int(input('Enter end number: '))
# step = int(input('Enter step: '))
#
# for dd in range(start,
#                 end,
#                 step):
#     print(dd)

# ! Fifth Example
# total = 0
# multiply = 1
# for dd in range(1,
#                 11):
#     total = total + dd  # => total += dd
#     # total += dd  # => total = total + dd
#     print(total,
#           dd)
#     multiply = multiply * dd # => multiply *= dd
#     # multiply *= dd # => multiply = multiply * dd
#     print(multiply)

# ! Sixth Example
# pieces = int(input('How many pieces of pizza, do you want? '))
# for slice in range(pieces):
#     print(f'{slice + 1}. slice of pizza')

# ! Seventh Example
# # * While loops
# i = 0
# while i < 5:
#     print()
#     i += 1

# ! Eighth Example
# piece = int(input('How many pieces of pizza, do you want? '))
# a = 1
# while a <= piece:
#     print(f'{a}. slice of pizza')
#     a += 1

# ! Ninth Example
# * first method
# answer = input('Do you want pizza? (yes/no) ')
# while answer.lower() == 'yes':
#     print('Here is your pizza, Bon Appétit')
#     answer = input("Do you want one more? (yes/no) ")

# * second method
# answer = bool(input('Do you want pizza? '))
# while answer == True:  # => while answer:
#     print('Here is your pizza, Bon Appétit')
#     answer = bool(input('Do you want one more? '))

# ! Tenth Example
# * pass, break, continue
# if True:
#     pass
# print('hi')

# ! Eleventh Example
# for dd in range(10):
#     name = input('Enter your name: ')
#     if name == 'Burak':
#         break
#     print(f'asked for {dd + 1}th student')

# ! Twelfth Example
# for dd in range(10):
#     name = input('Enter your name: ')
#     if name == 'burak':
#         print('Already registered user')
#         continue
#     surname = input('Enter your surname: ')
#     print(f'Welcome {name} {surname}')

# ! Thirteenth Example
# multiply = 1
# while True:
#     number = int(input("Enter a number: "))
#     if number == 0:
#         break
#     else:
#         multiply *= number
# print("Multiply of numbers is", multiply)

# ! Fourteenth Example
# for x in range(1, 11):
#     print("#{}".format(x))
#     for y in range(1, 11):
#         print("\t {}*{} = {}".format(x, y, x * y))

# ! Fifteenth Example
# last_number = int(input("Enter last number: "))
# for dd in range(1, last_number + 1):
#     if (dd % 3 == 0) & (dd % 5 == 0):
#         print(dd, "fiz & buzz")
#     elif dd % 3 == 0:
#         print(dd, "fiz")
#     elif dd % 5 == 0:
#         print(dd, "buzz")
#     else:
#         print(dd)

# ! Sixteenth Example
# try_ = 3
# correct_password = 'pyhton123'

# * First Method
# while try_ > 0:
#     password = input('Enter your password: ')
#     if password == correct_password:
#         print('Welcome to Python Bootcamp Program')
#         break
#     else:
#         try_ -= 1
#         print(f'You have {try_} tries left')
# if try_ == 0:
#     print('Your account is locked')

# * Second Method
# in python while loop, if break is not used, else block will be executed
# while try_ > 0:
#     password = input('Enter your password: ')
#     if password == correct_password:
#         print('Welcome to Python Bootcamp Program')
#         break
#     else:
#         try_ -= 1
#         print(f'You have {try_} tries left')
# else:
#     print('Your account is locked')

# ! Seventeenth Example

# * First Method (using if elif else)
# temp = 0
# while temp <= 200:
#     temp += 50
#     if temp == 100:
#         print('Owen temperature reached 100')
#         continue
#     elif temp == 200:
#         print('Owen temperature reached 200')
#         break
#     print(f'Owen temperature is {temp}')

# * Second Method (using match casse)
# temp = 0
# while temp <= 200:
#     temp += 50
#     match temp:
#         case 100:
#             print('Owen temperature reached 100')
#             continue
#         case 200:
#             print('Owen temperature reached 200')
#             break
#     print(f'Owen temperature is {temp}')

# ! Eighteenth Example
# * First method (Armstrong number)
# number = int(input('Enter a number: '))
# string_number = str(number)
# power = len(string_number)
# sum_ = 0
# for dd in string_number:
#     sum_ = sum_ + int(dd) ** power
#     print(dd,
#           sum_)
# if sum_ == number:
#     print(f'{number} is an Armstrong number')
# else:
#     print(f'{number} is not an Armstrong number')

# * Second method (Armstrong number)
# for number in range(1, 10000):
#     string_number = str(number)
#     power = len(string_number)
#     sum_ = 0

#     for dd in string_number:
#         sum_ = sum_ + int(dd) ** power
#     if sum_ == number:
#         print(f"{number} is an Armstrong number")
# else:
#     print(f"{number} is not an Armstrong number")


# ! Nineteenth Example
# * Count the number of 'a' in a sentence
# * First Method
# sentence = input('Enter a sentence: ')
# count = 0
# words = sentence.split()
# for word in words:
#     for letter in word:
#         if letter.lower() == 'a':
#             count += 1
# print(f"Number of 'a' in the '{sentence}' is {count}")

# * Second Method
# sentence = input('Enter a sentence: ')
# count = 0
# for letter in sentence:
#     if letter.lower() == 'a':
#         count += 1
# print(f"Number of 'a' in the '{sentence}' is {count}")

# ! Twentieth Example
# * Write a program to reverse a sentence
# * First Method
# sentence = input("Enter a sentence: ")
# reverse_sentence = ""

# for letter in range(len(sentence) - 1, -1, -1):
#     reverse_sentence += sentence[letter]

# print(f"Reverse version of the '{sentence}' is '{reverse_sentence}'")

# * Second Method
# sentence = input('Enter a sentence: ')
# reverse_sentence = ''
# for letter in sentence:
#     reverse_sentence = letter + reverse_sentence
# print(f"Reverse version of the '{sentence}' is '{reverse_sentence}'")

# ! Twenty-first Example
# * Guess the number game
# import random
#
# hold_number = random.randint(1, 10)
#
# while True:
#     number = int(input('Enter a number (1-10): '))
#     if number <= 0 or number >= 10:
#         print('You have to enter a number between 1 and 10')
#         continue
#     elif number == hold_number:
#         print('Congratulations!, you find correct number')
#         break
#     elif number < hold_number:
#         print('Too low')
#     elif number > hold_number:
#         print('Too high')
#     else:
#         print('Invalid number')

# ! Twenty-second Example
# sentence = ''
# while True:
#     word = input('Enter a word: ')
#     if word.lower() == 'quit':
#         break
#     else:
#         sentence += word + ' '
# print(sentence)
