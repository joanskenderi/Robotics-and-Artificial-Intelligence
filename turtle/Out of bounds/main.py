# Write an out-of-bounds game in turtle.

import turtle


def drawBox():
    box_drawer = turtle.Turtle()
    box_drawer.speed(10)
    box_drawer.color("red")
    box_drawer.penup()
    box_drawer.goto(-200, 200)
    box_drawer.pendown()

    for i in range(4):
        box_drawer.forward(400)
        box_drawer.right(90)
    box_drawer.penup()
    box_drawer.hideturtle()


my_turtle = turtle.Turtle()
screen = turtle.Screen()
score_turtle = turtle.Turtle()

drawBox()

angle = 10
step = 3
game_over = False


def turn_left():
    my_turtle(angle)


def turn_right():
    my_turtle(angle)


screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.listen()

while game_over != True:
    my_turtle.forward(step)
    x = my_turtle.xcor()
    y = my_turtle.ycor()

    if x > 200 or x < -200 or y > 200 or y < -200:
        game_over = True
        my_turtle.write("Out of bounds!")
