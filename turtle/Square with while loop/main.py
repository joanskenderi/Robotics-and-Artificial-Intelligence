# Write a program in turtle that uses while loop to draw a square.

import turtle

my_turtle = turtle.Turtle()

size = 100
angle = 90
count = 0

while count < 4:
    my_turtle.forward(size)
    my_turtle.left(angle)
    count = count + 1
