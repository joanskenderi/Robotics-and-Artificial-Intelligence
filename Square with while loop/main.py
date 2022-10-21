# Write a program in turtle that uses while loop to draw a square.

import turtle

myTurtle = turtle.Turtle()

size = 100
angle = 90

count = 0

while count < 4:
    myTurtle.forward(size)
    myTurtle.left(angle)
    count = count + 1
