import turtle as t

tim = t.Turtle()

########### Challenge 2 - Draw a Dashed Line ########

width = 10
for _ in range(15):
    tim.forward(width)
    tim.penup()
    tim.forward(width)
    tim.pendown()

screen = t.Screen()
t.exitonclick()
