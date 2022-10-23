# Write a program in turtle that draws a shell.

import turtle
import random

my_turtle = turtle.Turtle()

line_length = 1

for i in range(360):
    # Random color
    r = random.randint(0, 256)
    g = random.randint(0, 256)
    b = random.randint(0, 256)
    my_turtle.color(r, g, b)

    # Draw line
    my_turtle.goto(0, 0)
    my_turtle.forward(line_length)
    my_turtle.right(5)

    # Increase length of line
    line_length = line_length + 1
