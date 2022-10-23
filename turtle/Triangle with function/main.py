# Write a program in turtle that uses a function to draw a triangle.

import turtle

triangle = turtle.Turtle()


def draw_triangle(length):
    angle = 120
    for i in range(3):
        triangle.forward(length)
        triangle.left(angle)


draw_triangle(140)
