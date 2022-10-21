# Write a program in turtle that draws a square spiral.

import turtle

spiral = turtle.Turtle()

size = 10

for i in range(20):
    spiral.forward(size)
    spiral.right(90)
    size = size + 10
