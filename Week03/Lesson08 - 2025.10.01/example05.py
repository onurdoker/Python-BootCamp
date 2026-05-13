"""
This program uses the turtle library to draw a square with a turtle that moves forward and turns right at each corner.
"""

import time
import turtle

print("turtle library")
arrow = turtle.Turtle()
arrow.forward(100)
time.sleep(1)
arrow.right(90)
arrow.forward(100)
time.sleep(1)
arrow.right(90)
arrow.forward(100)
time.sleep(1)
arrow.right(90)
arrow.forward(100)
time.sleep(1)

screen = turtle.Screen()
screen.exitonclick()
