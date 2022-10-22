# Write ta program in turtle to simulate a race between three turtles.

import turtle
import random

# First turtle
first_turtle = turtle.Turtle()
first_turtle.penup()
first_turtle.color("red")
first_turtle.shape("turtle")
first_turtle.goto(-200, 90)
first_turtle.pendown()

# Second turtle
second_turtle = turtle.Turtle()
second_turtle.penup()
second_turtle.color("blue")
second_turtle.shape("turtle")
second_turtle.goto(-200, 50)
second_turtle.pendown()

# Third turtle
third_turtle = turtle.Turtle()
third_turtle.penup()
third_turtle.color("orange")
third_turtle.shape("turtle")
third_turtle.goto(-200, 10)
third_turtle.pendown()

# Logic for the race
for i in range(25):
    first_turtle.forward(random.randint(5, 20))
    second_turtle.forward(random.randint(5, 20))
    third_turtle.forward(random.randint(5, 20))
