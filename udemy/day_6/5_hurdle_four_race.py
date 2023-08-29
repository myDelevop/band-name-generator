from functions import *

while not at_goal():
    if wall_in_front():
        jump_high_wall()
    else:
        move()
