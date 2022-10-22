# Draw a random shape using turtle.

import turtle

shape = turtle.Turtle()


def draw_shape(length, number_of_sides):
    for i in range(number_of_sides):
        shape.forward(length)
        shape.right(360 / number_of_sides)


draw_shape(90, 7)
