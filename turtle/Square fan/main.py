# Write a program in turtle that draws a square fan.

import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(0)

angle = 10


def draw_square(size):
    for i in range(4):
        my_turtle.forward(size)
        my_turtle.right(90)


def draw_increasing_squares():
    length = 50

    for i in range(10):
        draw_square(length)
        length += 10


for i in range(36):
    draw_increasing_squares()
    my_turtle.right(angle)
