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


def jump_once():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


def at_goal():
    win_int = random.randint(0, 1)
    if win_int == 1:
        win = True
    else:
        win = False
    return win


# Call the function:
my_function()
