from paddle import Paddle
from turtle import Screen



screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600, startx=-200, starty=15)
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_up, "W")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(l_paddle.go_down, "S")


game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
