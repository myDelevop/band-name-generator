import turtle
import random

RADIUS = 100


def change_color(t: turtle.Turtle):
    r = random.random()
    g = random.random()
    b = random.random()

    t.color(r, g, b)


timmy = turtle.Turtle()
timmy.shape("turtle")
change_color(timmy)
timmy.speed("fastest")

for _ in range(40):
    timmy.circle(100)
    timmy.left(10)
    change_color(timmy)

screen = turtle.Screen()
screen.exitonclick()
