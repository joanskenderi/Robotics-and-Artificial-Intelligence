# Write a program in turtle that uses while loop to draw a triangle.

import turtle

my_turtle = turtle.Turtle()

length = 100
angle = 120
count = 0

while count < 3:
    my_turtle.forward(length)
    my_turtle.left(angle)
    count = count + 1
