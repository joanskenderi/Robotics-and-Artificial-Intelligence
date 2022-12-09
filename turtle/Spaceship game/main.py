# Write a spaceship game in turtle.

import turtle as turtle
from time import time
from random import randint

screen = turtle.Screen()

# Shooter
shooter = turtle.Turtle()
shooter.shape("turtle")
shooter.penup()
shooter.goto(-300, 0)
shooter.speed(0)


# Setup shooter listeners
def up():
    x, y = (shooter.xcor(), shooter.ycor())
    shooter.goto(x, y + 25)


def down():
    x, y = (shooter.xcor(), shooter.ycor())
    shooter.goto(x, y - 25)


screen.onkey(up, "Up")
screen.onkey(down, "Down")

# Setup bullets
bullets = []
SCREEN_END = 300
timestamp = time()


def calc_wait_time():
    return len(bullets) * 0.1


def fire_bullet():
    global timestamp
    if timestamp < time() - len(bullets) * 0.1:
        bullet = turtle.Turtle()
        bullet.penup()
        bullet.speed(0)
        bullet.hideturtle()
        bullet.goto(-215, shooter.ycor())
        bullet.showturtle()
        bullet.shape("circle")
        bullets.append(bullet)
        timestamp = time()


screen.onkey(fire_bullet, "space")

metheor = turtle.Turtle()
metheor.shape("square")
metheor.speed(0)
metheor.penup()


def check_collision():
    mx, my = metheor.xcor(), metheor.ycor()
    ml = mx - 50
    mr = mx + 50
    mu = my + 35
    md = my - 35

    for bullet in bullets:
        bx, by = bullet.xcor(), bullet.ycor()
        if ml < bx < mr and mu > by > md:
            bullet.hideturtle()
            bullets.remove(bullet)
            metheor.hideturtle()
            metheor.goto(210, randint(-200, 200))
            metheor.showturtle()
            return True
    return False


my_turtle = turtle.Turtle()
my_turtle.penup()
my_turtle.hideturtle()
my_turtle.speed(0)

# Listeners
points = 0
screen.listen()
while True:
    my_turtle.forward(1)
    for bullet in bullets:
        bullet.goto(bullet.xcor() + 15, bullet.ycor())
        if bullet.xcor() > SCREEN_END:
            bullet.hideturtle()
            bullets.remove(bullet)
    if check_collision():
        points += 1

turtle.done()
