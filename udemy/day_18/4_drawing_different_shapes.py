import turtle as t
from random import random

WEIGHT = 70


def change_color(turtle: t.Turtle):
    r = random()
    g = random()
    b = random()

    turtle.color(r, g, b)


def draw_shape(turtle: t.Turtle, shape_side):
    angle = 360 / shape_side
    for _ in range(shape_side):
        turtle.forward(WEIGHT)
        turtle.right(angle)


timmy = t.Turtle()
timmy.shape("turtle")
change_color(timmy)

for side in range(3, 11):
    print(side)
    change_color(timmy)
    draw_shape(timmy, side)

screen = t.Screen()
screen.exitonclick()
