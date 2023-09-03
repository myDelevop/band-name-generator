import turtle
from random import random, randint, choice

turtle.colormode(255)


def change_color(t: turtle.Turtle):
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    t.color(r, g, b)


def draw_shape(t: turtle.Turtle, shape_side):
    angle = 360 / shape_side
    for _ in range(shape_side):
        t.forward(20)
        t.right(angle)


def random_forward(t: turtle.Turtle):
    size = randint(20, 40)
    angle = choice([0, 90, 180, 270])
    # choice([15, 30, 45, 60, 90, 120, 150, 210, 240, 270, 300, 330, 360])
    t.forward(size)
    t.right(angle)
    change_color(t)


timmy = turtle.Turtle()
timmy.shape("turtle")
timmy.pensize(15)
timmy.speed("fastest")
change_color(timmy)


for i in range(200):
    random_forward(timmy)

screen = turtle.Screen()
screen.exitonclick()
