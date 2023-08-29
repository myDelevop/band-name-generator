from functions import *


# first while in order to avoid infinite loops if there is no right-side wall
while front_is_clear():
    move()
turn_left()


while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
