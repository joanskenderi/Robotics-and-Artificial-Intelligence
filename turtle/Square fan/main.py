# Write a program in turtle that draws a square fan.

import turtle

square = turtle.Turtle()
angle = 10

square.speed(0)


def draw_square(size):
    for i in range(4):
        square.forward(size)
        square.right(90)


def draw_increasing_squares():
    length = 50
    for i in range(10):
        draw_square(length)
        length += 10


for i in range(36):
    draw_increasing_squares()
    square.right(angle)
