# Write a program in turtle that draws a shell.

import turtle
import random

shell = turtle.Turtle()

line_length = 1

for i in range(360):
    # Random color
    r = random.randint(0, 256)
    g = random.randint(0, 256)
    b = random.randint(0, 256)
    shell.color(r, g, b)

    # Draw line
    shell.goto(0, 0)
    shell.forward(line_length)
    shell.right(5)

    # Increase length of line
    line_length = line_length + 1
