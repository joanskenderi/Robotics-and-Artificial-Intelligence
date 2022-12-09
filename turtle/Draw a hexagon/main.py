# Write a program in turtle that draws a hexagon.

import turtle

my_turtle = turtle.Turtle()

num_sides = 6
side_length = 70
angle = 360 / num_sides

for i in range(num_sides):
    my_turtle.forward(side_length)
    my_turtle.right(angle)
