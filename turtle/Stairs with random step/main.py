# Write a program in turtle that draws stairs with random step.

import turtle
import random

stairs = turtle.Turtle()

angle = 90
steps = 10

for i in range(steps):
    length = random.randint(10, 40)
    stairs.forward(length)
    stairs.left(angle)

    length = random.randint(10, 40)
    stairs.forward(length)
    stairs.right(angle)
