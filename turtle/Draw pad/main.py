# Write a draw pad program in turtle.

import turtle

wn = turtle.Screen()


def dragging(x, y):
    pad.ondrag(None)
    pad.setheading(pad.towards(x, y))
    pad.goto(x, y)
    pad.ondrag(dragging)


def h1(x, y):
    pad.penup()
    pad.goto(x, y)
    pad.pendown()


wn.onclick(h1)
pad = turtle.Turtle('turtle')
pad.speed('fastest')
pad.color("purple")
pad.pensize(1)
pad.shape("circle")
pad.ondrag(dragging)
