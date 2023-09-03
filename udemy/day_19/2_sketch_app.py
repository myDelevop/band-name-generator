import turtle as t

tim = t.Turtle()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def counter_clock_wise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def clock_wise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear():
    tim.clear()
    tim.pu()
    tim.home()
    tim.pd()


screen = t.Screen()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=counter_clock_wise)
screen.onkey(key="d", fun=clock_wise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
