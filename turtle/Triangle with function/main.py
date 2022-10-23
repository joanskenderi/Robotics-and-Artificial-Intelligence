# Write a program in turtle that uses a function to draw a triangle.

import turtle

my_turtle = turtle.Turtle()


def draw_triangle(length):
    angle = 120
    
    for i in range(3):
        my_turtle.forward(length)
        my_turtle.left(angle)


draw_triangle(140)
