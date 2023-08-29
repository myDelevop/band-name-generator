from functions import *

while not at_goal():
    if wall_in_front():
        jump_with_no_move()
    else:
        move()
