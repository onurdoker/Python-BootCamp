# ! First Example
# * importing libraries
# import random

# print(random.randint(1, 5))

# * while importing a library, you can use it as an alias
# import random as rd

# print(rd.randint(1, 5))

# ! Second Example
# * importing all functions from a library
# from random import *  # import all functions from random library

# print(randint(1, 5))
# print(randrange(2, 50, 2))

# * importing specific functions from a library
# from random import randint  # import randint function from random library

# print(randint(5, 50))

# ! Third Example
# * Mathematical Module
# import math  # * math library

# print("Pi Number: ", math.pi)
# print("Power of the number: ", math.pow(5, 6))

# print("Square root of the number: ", math.sqrt(16))

# print("Round the number: ", round(4.501))

# print("Calculating cos an angle: ", math.cos(math.radians(90)))

# ! Fourth Example
# import random  # * random library

# print(
#     "random a number between 0 - 1: ", random.random()
# )  # * random float number between 0 and 1

# print(
#     "random a number between 0 - 100: ", random.randint(1, 100)
# )  # * random integer number between 1 and 100

# print(
#     "random a float number between 1 - 5: ", random.uniform(1, 5)
# )  # * random float number between 1 and 5

# colors = ["red", "yellow", "pink"]
# chosen_color = random.choice(colors)
# print("chosen color: ", chosen_color)

# random.shuffle(colors)
# print("shuffled colors: ", colors)

# ! Fifth Example
# * datetime module
# import datetime  # * using for date and time

# now_ = datetime.datetime.now()
# print("Now: ", now_)
# print("Year: ", now_.year)
# print("Month: ", now_.month)
# print("Day: ", now_.day)
# print("Hour: ", now_.hour)
# print("Minutes: ", now_.minute)
# print("Seconds: ", now_.second)
# print("Microseconds: ", now_.microsecond)
# print("Date: ", now_.date())
# print("Which day of week: ", now_.weekday())
# print("Which day of week: ", now_.strftime("%A"))
# print("Which mount: ", now_.strftime("%B"))
# print("Which day of mount: ", now_.strftime("%d"))
# print("Format of time: ", now_.strftime("%d/%m/%Y"))
# print("Hour format: ", now_.strftime("%H:%M:%S"))
# print(
#     "Week Day: ", now_.strftime("%A").replace("Wednesday", "Carsamba")
# )  # to change the day name
# print("Month: ", now_.strftime("%B").replace("October", "Kasim"))

# ! Sixth Example
# import time
# import turtle

# print("turtle library")
# arrow = turtle.Turtle()
# arrow.forward(100)
# time.sleep(1)
# arrow.right(90)
# arrow.forward(100)
# time.sleep(1)
# arrow.right(90)
# arrow.forward(100)
# time.sleep(1)
# arrow.right(90)
# arrow.forward(100)
# arrow.right(90)

# for _ in range(3):
#     arrow.forward(100)
#     arrow.left(120)
#     time.sleep(1)

# screen = turtle.Screen()

# screen.exitonclick()

# ! Seventh Example
# import math

# try:
#     radius = float(input("Enter the radius of the circle: "))
#     if radius <= 0:
#         raise ValueError("Radius must be greater than 0")
#     circle_area = math.pi * math.pow(radius, 2)
#     circle_circumference = 2 * math.pi * radius
#     print(f"\nCircle knowledge:")
#     print(f"Circle radius: {radius}")
#     print(f"Circle circumference: {circle_circumference:.3f}")
#     print(f"Circle square: {circle_area:.2f}")

#     print("\nSquare root and power of the radius:")
#     sqrt_ = math.sqrt(radius)
#     power_ = math.pow(radius, 2)
#     cube = math.pow(radius, 3)
#     print(f"Square root of the radius: {sqrt_: .2f}")
#     print(f"Power of the radius: {power_: .2f}")
#     print(f"Cube of the radius: {cube:.2f}")

#     print(f"\nTrigonometric functions: ")
#     angel = float(input("Enter the angel (degree): "))
#     angel_rad = math.radians(angel)
#     print(f"Sine of the radius: {math.sin(angel_rad): .2f}")
#     print(f"Cosine of the radius: {math.cos(angel_rad): .2f}")
#     print(f"Tangent of the radius: {math.tan(angel_rad): .2f}")

# except ValueError as error:
#     print(f"Error: {error}")

# print("Calculations ended")

# ! Eighth Example
# from datetime import datetime

# birthday = input("Enter your birthday (dd/mm/yyyy): ")
# day, month, year = map(int, birthday.split("/"))
# print(day, month, year)

# bd_date = datetime(year, month, day)
# print(bd_date)

# today = datetime.now()
# print("today", today)

# this_year_bd = bd_date.replace(year=today.year)
# print("this year birth day: ", this_year_bd)

# if this_year_bd < today:
#     print(f"{(today - this_year_bd).days} days have passed since your birthday ")

#     this_year_bd = this_year_bd.replace(year=today.year + 1)

# print(f"There are {(this_year_bd - today).days} days left until your birthday")

# ! Ninth Example
# import random
# import string


# def password_generator(length):
#     character = string.ascii_letters + string.digits + "!@#$%"
#     return "".join(random.choice(character) for _ in range(length))


# try:
#     length_ = int(input("Enter the length of the password: "))
#     print("Your password: ", password_generator(length_))
# except:
#     print("Please enter a valid number")

# ! Tenth Example
# import random

# try_number = 0
# symbols = [1, 2, 3, 4, 5, 6, 7]

# while True:
#     input("Press enter to roll the dice ")
#     result = [str(random.choice(symbols)) for _ in range(3)]
#     print(" | ".join(result))
#     try_number += 1

#     if result[0] == result[1] == result[2]:
#         print("You win!")
#         print("Try Number: ", try_number)
#     else:
#         print("You lose!")

# ! Eleventh Example
# import json
#
# # * Converting python object to json string

# data = {"name": "Ali", "age": 30, "cities": ["Istanbul", "Ankara", "Izmir"]}
# print(data)
# json_str = json.dumps(data, ensure_ascii=False, indent=2)
# print("JSON Strint:\n", json_str, "\n", type(json_str))
#
# # * Converting json string to python object
# parsed = json.loads(json_str)
# print(type(parsed))  # <class 'dict'>
# print(parsed["name"])  # Ali
