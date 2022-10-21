# Write a program in turtle that uses while loop to draw a square.

import turtle

square = turtle.Turtle()

size = 100
angle = 90

count = 0

while count < 4:
    square.forward(size)
    square.left(angle)
    count = count + 1
