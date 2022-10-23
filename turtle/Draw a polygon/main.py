# Draw a polygon using turtle.

import turtle

polygon = turtle.Turtle()


def draw_shape(length, number_of_sides):
    for i in range(number_of_sides):
        polygon.forward(length)
        polygon.right(360 / number_of_sides)


draw_shape(90, 7)
