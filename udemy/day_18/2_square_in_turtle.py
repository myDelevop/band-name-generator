from turtle import Turtle, Screen

width = 100

timmy = Turtle()
timmy.shape("turtle")
timmy.color("blue")

for _ in range(4):
    timmy.forward(width)
    timmy.right(90)

screen = Screen()
screen.exitonclick()
