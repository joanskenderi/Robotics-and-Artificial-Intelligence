# Write a program in turtle that draws a polygon.

import turtle

my_turtle = turtle.Turtle()


def draw_shape(length, number_of_sides):
    for i in range(number_of_sides):
        my_turtle.forward(length)
        my_turtle.right(360 / number_of_sides)


draw_shape(90, 7)
