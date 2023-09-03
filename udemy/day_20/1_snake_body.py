from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

""""
t1 = Turtle(shape="square")
t1.color("white")

t2 = Turtle(shape="square")
t2.color("white")
t2.goto(x=-20, y=0)

t3 = Turtle(shape="square")
t3.color("white")
t3.goto(x=-40, y=0)
"""

# Or, with a loop

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

for pos in starting_positions:
    turtle = Turtle(shape="square")
    turtle.color("white")
    turtle.goto(pos)

screen.exitonclick()
