# Write a program in turtle that chases the mice after click.

import turtle

screen = turtle.Screen()
my_turtle = turtle.Turtle()

my_turtle.color("purple")
my_turtle.pensize(3)
my_turtle.shape("circle")


def h1(x, y):
    my_turtle.goto(x, y)


screen.onclick(h1)
screen.listen()
