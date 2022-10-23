# Write a program in turtle that generates a polygon in each click.

import turtle
import random

my_turtle = turtle.Turtle()
my_turtle.speed()
screen = turtle.Screen()


def draw_shape(x, y):
    size = random.randint(10, 100)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    number_of_sides = random.randint(3, 10)
    angle = 360 / number_of_sides

    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.color(r, g, b)
    my_turtle.begin_fill()

    for i in range(number_of_sides):
        my_turtle.forward(size)
        my_turtle.left(angle)
    my_turtle.end_fill()


screen.onclick(draw_shape)
