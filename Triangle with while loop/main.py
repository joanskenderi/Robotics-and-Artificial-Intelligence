# Write a program in turtle that uses while loop to draw a triangle.

import turtle

myTurtle = turtle.Turtle()

length = 100
angle = 120

count = 0

while count < 3:
    myTurtle.forward(length)
    myTurtle.left(angle)
    count = count + 1
