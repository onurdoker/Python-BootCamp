# ! First Example
# print('Hello TechIstanbul')
# print('How are you?')

# ! Second Example
# ! Main data types in Python
# * Integer => int()
# print(34)
# print(type(34))
# print(-28)
# print(type(-28))

# * Float => float()
# print(34.2)
# print(type(34.2))
# print(-28.3)
# print(type(-28.3))

# * String => str()
# print("Hello")
# print(type("Hello"))
# print('24')
# print(type('24'))

# * Boolean => bool()
# print(True)
# print(type(True))
# print(False)
# print(type(False))

# ! Third Example
# print('my name is : Onur')
# print('my surname is : Doker')
# print('my age is : 48')
# print('my country is : Turkey')

# ! Fourth Example
# ! Operators
# * Arithmetical Operators
# print(3 + 4)
# print(3 - 4)
# print(3 * 4)
# print(3 / 4)  # ? Float Division

# print(5 ** 2)
# print(5 // 2)  # ? Integer Division
# print(5 % 2)  # ? Modulo

# * Comparison Operators
# print(3 > 4)
# print(3 < 4)
# print(3 == 4)
# print(3 != 4)
# print(3 >= 4)
# print(3 <= 4)

# * Assignment Operators
# x = 5
# print(x)

# * Logical Operators
# * and or not
# print((20 >= 18) and (3 > 1))
# print((80 >= 70) or (3 >= 50))
# print(not (20 >= 18))
# print(not (True))  # False

# * Membership Operators
# print("TechIstanbul" in "TechIstanbul")
# print("TechIstanbul" not in "TechIstanbul")

# ! Fifth Example
# * RULES
# 1. start with letter and _
# 2. don't start with numbers
# 3. don't use Turkish letters
# 4. don't use special characters (except _)
# 5. Case-sensitive
# 6. don't use reserved keywords (if, else, while, for, def, class, etc.)
# 7. use snake_case

# number = int("123")
# print(number)
# print(type(number))

# number = str(123)
# print(number,
#       type(number))

# number = float(123)
# print(number,
#       type(number))

# number = bool(123)
# print(number,
#       type(number))

# ! Sixth Example
# number = 10
# print(number)

# number += 5  # number = number + 5
# print(number)

# number -= 5  # number = number - 5
# print(number)

# number *= 5  # number = number * 5
# print(number)

# number /= 5  # number = number / 5
# print(number)

# number **= 5  # number = number ** 5
# print(number)

# number //= 5  # number = number // 5
# print(number)

# number %= 5  # number = number % 5
# print(number)

# name = 'Tech'
# name += 'Istanbul'
# print(name)

# ! Seventh Example
# * Typecasting
# * int() str() float() bool()

# number = '35'
# number = int(number)
# print('number :',
#       number,
#       type(number))

# ! Eighth Example
# * input() take data from user

print('What is your name?')
name = input()
print('Nice to meet you',
      name)

print('How old are you?')
yas = input()  # input always takes data as string
yas = int(yas)
print(yas * 2)

name = input('Name : ')
age = input('Age : ')
print('Hello',
      name,
      'you are',
      age,
      'years old')