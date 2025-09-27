# ! First Example
# number = 5
# print(number * number)
#
# number = 8
# print(number * number)
#
# number = 10
# print(number * number)


# ! Second Example
# * Function
# def calculate_square(number):
#     return number * number
#
#
# print(calculate_square(5))
# print(calculate_square(8))
# print(calculate_square(10))

# ! Third Example
# * without parameters and not return value
# def greetings():
#     print('Hello Python Bootcamp Program')
#     print('This bootcamp was organized btTechIstanbul and Ecodation')
#
#
# greetings()
# greetings()
# greetings()
# print(greetings,
#       type(greetings))

# ! Fourth Example
# * with parameters and not return value
# def greeting(name):
#     print(f'Hello {name}')
#
#
# greeting('Onur')
# greeting('Burak')
# greeting('Timur')
# a = greeting('onur')
# print(a,
#       type(a))


# ! Fifth Example
# * with parameters and not return value
# def sum_of_two_numbers(number1,
#                        number2):
#     calculate = number1 + number2
#     print(f'{number1} + {number2} = {calculate}')
#
#
# sum_of_two_numbers(3,
#                    5)
# sum_of_two_numbers(10,
#                    20)

# ! Sixth Example
# * without parameters and return value
# def greeting():
#     name = input('Enter your name: ')
#     print('Welcome',
#           name)
#     return name
#
#
# greeting()
# print(greeting(),
#       type(greeting()))

# ! Seventh Example
# * with parameters and return value

# def square(number):
#     return number * number
#
#
# print(square(5))
#
# square5 = square(5)
# print(square5,
#       type(square5))

# ! Eighth Example
# def multiply(number1,
#              number2):
#     return number1 * number2
#
#
# print(multiply(3,
#                5))
# there_times_five = multiply(3,
#                             5)
# print(there_times_five,
#       type(there_times_five))


# ! Ninth Example
# def power_control(number,
#                   power):
#     if number % power == 0:
#         return number // power
#
#
# print(power_control(10,
#                     2))
# print(power_control(10,
#                     3))


# ! Tenth Example
# def greeting(name):
#     print(f'Hi {name} \nWelcome to Python Bootcamp Program')
#     if len(name) < 5:
#         return True
#     else:
#         return False
#
#
# name = input('Enter your name: ')
# answer = greeting(name)
# if answer:
#     print('Your name is too short')
# else:
#     print('Your name is valid')


# ! Eleventh Example
# def sum_of_two_numbers(number1,
#                        number2):
#     calculate = number1 + number2
#     return calculate
#
#
# print(sum_of_two_numbers(3,
#                          5))


# ! Twelfth Example
# Snake case => function_name
# Camel case => functionName
# Pascal case => FunctionName

# def calculate_age(birth_year):
#     age = 2025 - birth_year
#     return age
#
#
# print('if you born at 1990, you are ',
#       calculate_age(1990))

# ! Thirteenth Example
# def calculate_circle_area(radius):
#     pi = 3.14
#     square = (pi * radius ** 2)
#     return square
#
#
# print(calculate_circle_area(5))

# ! Fourteenth Example
# TODO CHECK CODE!!!!
# def calculate_sum(a,
#                   b):
#     return a + b
#
#
# def calculate_difference(a,
#                          b):
#     return a - b
#
#
# def calculate_product(a,
#                       b):
#     return a * b
#
#
# def calculate_quotient(a,
#                        b):
#     return a / b
#
#
# def calculation(a,
#                 b,
#                 process):
#     process = input('Enter process (+,-,*,/): ')
#
#     def numbers():
#         return float(input('Enter a number: '))
#
#     a = numbers()
#     b = numbers()
#     if process == '+':
#         calculate_sum(a,
#                       b)
#     elif process == '-':
#         calculate_difference(a,
#                              b)
#     elif process == '*':
#         calculate_product(a,
#                           b)
#     elif process == '/':
#         calculate_quotient(a,
#                            b)
#     else:
#         print('Invalid process')

# ! Fifteenth Example
# def calculate_square(radius=1,
#                      pi=3.14):
#     square = pi * radius ** 2
#     return square
#
#
# print(calculate_square())
# print(calculate_square(5))
# print(calculate_square(5,
#                        3.1))

# ! Sixteenth Example
# def greeting(name='Guest'):
#     print(f'Hi {name} \nWelcome to Python Bootcamp Program')
#
#
# greeting('Onur')
# greeting()

# ! Seventeenth Example
# * Arguments (positional arguments)
# def calculate_sum(*args):
#     print(args,
#           type(args))
#     total = 0
#     for arg in args:
#         total += arg
#     print('total: ',
#           total)
#     return total
#
#
# calculate_sum(5,
#               10,
#               15)
# calculate_sum(5,
#               10,
#               15,
#               20,
#               25)

# ! Eighteenth Example
# def calculate_sum(x,
#                   *args):
#     print(args,
#           type(args))
#     total = 0
#     for arg in args:
#         total += arg * x
#     print('total: ',
#           total)
#     return total
#
#
# calculate_sum(5,
#               10,
#               15)
# calculate_sum(5,
#               10,
#               15,
#               20,
#               25)


# ! Nineteenth Example

# def calculate_average(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     average = total / len(args)
#     print('average: ',
#           average)
#     return average
#
#
# calculate_average(5,
#                   10,
#                   15)
# calculate_average(5,
#                   10,
#                   15,
#                   20,
#                   25)

# ! Twentieth Example
# * **kwargs
# def student_knowledge(**kwargs):
#     print(kwargs,
#           type(kwargs))
#     for key, value in kwargs.items():
#         print(f'{key} : {value}')
#
#
# student_knowledge(name='Onur',
#                   surname='doker',
#                   age=48,
#                   department='Chemical Engineering',
#                   attendance=True,
#                   average=3.7)

# ! Twenty First Example
# def item_entry(**kwargs):
#     item = {}
#     for key, value in kwargs.items():
#         item[key] = value
#     return item
#
#
# laptop = item_entry(name='Macbook Pro',
#                     item_price=25000,
#                     stock=30)
# print(laptop)

# ! Twenty Second Example
# def student_card(*args,
#                  **kwargs):
#     print(args,
#           type(args))
#     print(kwargs,
#           type(kwargs))
#
#
# student_card('YOK cart',
#              student_name='Onur',
#              student_surname='Doker',
#              student_department='Chemical Engineering')

# ! Twenty Third Example
# * Lambda => anonymous function

# calculate_square = lambda number: number * number
# print(calculate_square(5))
# print(calculate_square(8))
#
# calculate_sum = lambda number1,
#                        number2: number1 + number2
# print(calculate_sum(3,
#                     5))
# print(calculate_sum(10,
#                     20))

# ! Twenty Fourth Example
# students = [('onur',
#              30),
#             ('ada',
#              20),
#             ('mert',
#              25),
#             ('fatima',
#              22)]
#
# sorted_students = sorted(students,
#                          key=lambda x: x[1],
#                          reverse=True)
# print(sorted_students)

# ! Twenty Fifth Example
# numbers = [1,
#            2,
#            3,
#            4,
#            5,
#            6,
#            7,
#            8,
#            9,
#            10]
# even_numbers = list(filter(lambda x: x % 2 == 0,
#                            numbers))
# print(even_numbers)

# ! Twenty Sixth Example

# calculate_square = list(map(lambda x: x * 2,
#                             numbers))
# print(calculate_square)

# ! Twenty Seventh Example
# multiply_table = [[i * j for j in range(1,
#                                         4)] for i in range(1,
#                                                            4)]
# print('Multiply Table: ')
# for row in multiply_table:
#     print(row)

# ! Twenty Eighth Example
# def control_password(password):
#     if password < 8:
#         return 'Password has at least 8 characters'
#     elif password.isnumeric():
#         return 'Password has at least one letter'
#     elif password.isalnum():
#         return 'Password has at least one special character'
#     elif password.isalpha():
#         return 'Password has at least one number'
#     elif password.lower() == password:
#         return 'Password has at least one uppercase letter'
#     elif password.upper() == password:
#         return 'Password has at least one lowercase letter'
#     else:
#         return 'Password is valid'
#
#
# password = 'Python123'
# control_password(password)
# print(control_password(password))


# ! Twenty Ninth Example
# Fibonacci Series
# def fibonacci_series(number):
#     series = []
#     a, b = 0, 1
#     for _ in range(number):
#         series.append(a)
#         a, b = b, a + b
#     return series
#
#
# print(fibonacci_series(10))

# ! Thirtieth Example
# def factorial(number):
#     if number == 0 or number == 1:
#         return 1
#     else:
#         return number * factorial(number - 1)
#
#
# print(factorial(15))

# ! Thirty First Example
# write reverse

# def reverse_string(string):
#     if len(string) == 0:
#         return string
#     else:
#         return string[-1] + reverse_string(string[0:len(string) - 1])
#         # return string[-1] + reverse_string(string[:-1])
#
# print(reverse_string('merhaba'))

# ! Thirty Second Example
# find maximum number
# def find_max(*args):
#     if len(args) == 0:
#         return None
#     else:
#         max_number = args[0]
#         for arg in args:
#             if arg > max_number:
#                 max_number = arg
#     return max_number
#
#
# print(find_max(1,
#                2,
#                6,
#                4,
#                5))

# ! Thirty Third Example

# def student_score_average(student):
#     total = 0
#     for score in student['scores']:
#         total += score
#     average_score = total / len(student['scores'])
#     return average_score
#
#
# student = {'name': 'Onur', "scores": [70,
#                                       85,
#                                       90,
#                                       65]}
# average = student_score_average(student)
# print(f'{student['name']} \n{average}')

# ! Thirty Fourth Example

# TODO CHECK CODE!!!!
# def value_changer(colors,
#                   treng):
#     for key, value in colors.items():
#         colors[value] = treng[value]
#     return colors
#
#
# treng = {'red': 'kirmizi', 'green': 'yesil', 'blue': 'mavi'}
# colors = {'red': '#FF0000', 'green': '#00FF00', 'blue': '#0000FF'}
# result = value_changer(colors,
#                        treng)
# print(result)
