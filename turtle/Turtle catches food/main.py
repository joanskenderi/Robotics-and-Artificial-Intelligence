# Write program in turtle in which a turtle eats food and each food is one point.

from turtle import *
from random import randint
from math import sqrt


def create_head():
    my_turtle = Turtle()
    my_turtle.shape("turtle")
    my_turtle.penup()
    my_turtle.color("red")
    return my_turtle


def move_turtle_randomly(t):
    x = randint(-200, 200)
    y = randint(-200, 200)
    my_turtle.penup()
    my_turtle.hideturtle()
    my_turtle.setx(x)
    my_turtle.sety(y)
    my_turtle.showturtle()


def check_distance(t1, t2):
    x1 = t1.xcor()
    x2 = t2.xcor()
    y1 = t1.ycor()
    y2 = t2.ycor()
    d = (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)
    return sqrt(d)


screen = Screen()

# Points
points = Turtle()
points.hideturtle()
points.penup()
points.goto(200, 200)
points.color("blue")
text = points.write("You got 0 points")

# Food
food = Turtle()
food.shape("circle")
food.color("green")
food.speed(0)
head = create_head()


def up():
    head.setheading(90)


def left():
    head.setheading(180)


def right():
    head.setheading(0)


def down():
    head.setheading(270)


screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.listen()

min_distance = 20
counter = 0
head_speed = 1000
head_step = 2

while True:
    head.speed(head_speed)
    head.forward(head_step)
    d = check_distance(head, food)

    if d < min_distance:
        counter += 1
        if head_speed > 0:
            head_speed -= 1
        if head_step < 6:
            head_step += 0.2

        points.clear()
        points.write("you got " + str(counter) + " points", font=("Arial", 15, "normal"))
        move_turtle_randomly(food)

done()
