# Write a program in turtle that draws a square spiral.

import turtle

my_turtle = turtle.Turtle()

size = 10

for i in range(20):
    my_turtle.forward(size)
    my_turtle.right(90)
    size = size + 10
