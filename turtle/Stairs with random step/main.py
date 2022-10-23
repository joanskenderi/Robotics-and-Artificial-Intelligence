# Write a program in turtle that draws stairs with random step.

import turtle
import random

my_turtle = turtle.Turtle()

angle = 90
steps = 10

for i in range(steps):
    length = random.randint(10, 40)
    my_turtle.forward(length)
    my_turtle.left(angle)

    length = random.randint(10, 40)
    my_turtle.forward(length)
    my_turtle.right(angle)
