import random


def my_function():
    print("Hello")
    print("Bye")


def move():
    print("Movement Simulation")


def turn_left():
    print("turn left simulation")


def turn_around():
    turn_left()
    turn_left()


def turn_right():
    turn_around()
    turn_left()


def jump_with_no_move():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


def jump_once():
    move()
    jump_with_no_move()


def jump_high_wall():
    turn_left()
    steps = 0
    while not right_is_clear():
        move()
        steps += 1
    turn_right()
    move()
    turn_right()
    for i in range(0, steps):
        move()
    turn_left()


def at_goal():
    win_int = random.randint(0, 1)
    if win_int == 1:
        win = True
    else:
        win = False
    return win


def wall_in_front():
    return at_goal()


def right_is_clear():
    return at_goal()

def front_is_clear():
    return at_goal()

# Call the function:
my_function()

