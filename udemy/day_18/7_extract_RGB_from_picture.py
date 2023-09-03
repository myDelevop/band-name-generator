# import colorgram
import turtle
import random

X_POS = -252
Y_POS = -170
X_GAP = 55
Y_GAP = 36
turtle.colormode(255)

""""
colors = colorgram.extract('./image.jpg', 12 * 7)

colors_list = []
for color in colors:
    t = (color.rgb.r, color.rgb.g, color.rgb.b)
    colors_list.append(t)

print(colors_list)

Commented because we have already extracted colors from the image
"""


def change_color(t: turtle.Turtle):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    t.color(r, g, b)


colors_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102), (66, 64, 60), (219, 178, 183), (178, 198, 202), (112, 139, 141), (254, 194, 0)]

timmy = turtle.Turtle()
timmy.shape("turtle")
timmy.hideturtle()  # if you want

timmy.pu()
timmy.setpos((X_POS, Y_POS))
timmy.pd()

for i in range(0, 10):
    if i != 0:
        timmy.setpos((X_POS, timmy.pos()[1] + Y_GAP))
    timmy.pu()
    timmy.pd()
    for _ in range(0, 10):
        timmy.dot(20, random.choice(colors_list))
        timmy.pu()
        timmy.forward(X_GAP)


screen = turtle.Screen()
screen.exitonclick()
