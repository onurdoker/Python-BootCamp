print('Hello TechIstanbul')
print('How are you?')

# ! Main data types in Python
# * Integer => int()
print(34)
print(type(34))
print(-28)
print(type(-28))

# * Float => float()
print(34.2)
print(type(34.2))
print(-28.3)
print(type(-28.3))

# * String => str()
print("Hello")
print(type("Hello"))
print('24')
print(type('24'))

# * Boolean => bool()
print(True)
print(type(True))
print(False)
print(type(False))

print('TechIstanbul')
print('Ecodation')

print('my name is : Onur')
print('my surname is : Doker')
print('my age is : 48')
print('my country is : Turkey')


# ! Operators
# * Arithmetical Operators
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4) # ? Float Division

print(5 ** 2)
print(5 // 2) # ? Integer Division
print(5 % 2) # ? Modulo

# * Comparison Operators
print(3 > 4)
print(3 < 4)
print(3 == 4)
print(3 != 4)
print(3 >= 4)
print(3 <= 4)

# * Assignment Operators
x = 5
print(x)

# * Logical Operators
# and or not
print ((20 >= 18) and ( 3 > 1))
print ((80 >= 70) or ( 3 >= 50))
print(not(20 >= 18))
print(not(True)) # False

# * Membership Operators
print("TechIstanbul" in "TechIstanbul")
print("TechIstanbul" not in "TechIstanbul")


#  * Typecasting
# * int() str() float() bool()
number = int("123")
print(number)
print(type(number))

number = str(123)
print(number, type(number))

number = float(123)
print(number, type(number))

number = bool(123)
print(number, type(number))


# * input() take data from user
print('What is your name?')
name = input()
print('Nice to meet you', name)

print('How old are you?')
yas = input() # input always takes data as string
yas = int(yas)
print(yas * 2)


name = input('Name : ')
age = input('Age : ')
print('Hello', name, 'you are', age, 'years old')
