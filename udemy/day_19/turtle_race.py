from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color: ").lower()


colors = ["red", "orange", "yellow", "green", "blue", "purple"]

is_race_on = False

red = Turtle(shape="turtle")
red.penup()
red.goto(x=-240, y=27)
# red.pendown()
red.color("red")

orange = Turtle(shape="turtle")
orange.penup()
orange.goto(x=-240, y=81)
# orange.pendown()
orange.color("orange")

yellow = Turtle(shape="turtle")
yellow.penup()
yellow.goto(x=-240, y=135)
# yellow.pendown()
yellow.color("yellow")

green = Turtle(shape="turtle")
green.penup()
green.goto(x=-240, y=-27)
# green.pendown()
green.color("green")

blue = Turtle(shape="turtle")
blue.penup()
blue.goto(x=-240, y=-81)
# blue.pendown()
blue.color("blue")

purple = Turtle(shape="turtle")
purple.penup()
purple.goto(x=-240, y=-135)
# purple.pendown()
purple.color("purple")

if bet:
    is_race_on = True

winners = []

while is_race_on:
    ran_distance_red = random.randint(0,10)
    ran_distance_orange = random.randint(0,10)
    ran_distance_yellow = random.randint(0,10)
    ran_distance_green = random.randint(0,10)
    ran_distance_blue = random.randint(0,10)
    ran_distance_purple = random.randint(0,10)

    red.forward(ran_distance_red)
    orange.forward(ran_distance_orange)
    yellow.forward(ran_distance_yellow)
    green.forward(ran_distance_green)
    blue.forward(ran_distance_blue)
    purple.forward(ran_distance_purple)

    if red.pos()[0] > 222:
        winners.append("red")
    if orange.pos()[0] > 222:
        winners.append("orange")
    if yellow.pos()[0] > 222:
        winners.append("yellow")
    if green.pos()[0] > 222:
        winners.append("green")
    if blue.pos()[0] > 222:
        winners.append("blue")
    if purple.pos()[0] > 222:
        winners.append("purple")

    if len(winners) != 0:
        is_race_on = False

print("The winners are... " + str(winners))

if winners.__contains__(bet):
    print(f"You've won! The {winners} turtle/s are the winner!")
else:
    print(f"You've lost! The {winners} turtle/s are the winner!")

screen.exitonclick()
