# Draw a hexagon using turtle.

import turtle

hexagon = turtle.Turtle()

num_sides = 6
side_length = 70
angle = 360 / num_sides

for i in range(num_sides):
    hexagon.forward(side_length)
    hexagon.right(angle)
