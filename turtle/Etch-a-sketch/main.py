# Write an Etch-A-Sketch program in turtle.

import turtle

my_turtle = turtle.Turtle()
screen = turtle.Screen()

distance = 10
angle = 10


def move_forward():
    my_turtle.forward(distance)


def move_backward():
    my_turtle.backward(distance)


def press_left_key():
    my_turtle.left(angle)


def press_right_key():
    my_turtle.right(angle)


screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(press_left_key, "Left")
screen.onkey(press_right_key, "Right")

screen.listen()
