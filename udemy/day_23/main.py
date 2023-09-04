import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600, startx=-300, starty=15)
screen.tracer(0)


player = Player()
scoreboard = ScoreBoard()

screen.listen()
screen.onkeypress(player.move, "Up")


game_is_on = True
num_of_loops = 0
cars = []

while game_is_on:
    if num_of_loops % 6 == 0:
        car = CarManager()
        cars.append(car)

        car.set_speed(cars[0].distance)

    for c in cars:
        c.move()

    # Detect when the turtle collides with a car
    for c in cars:
        if player.distance(c) < 25:
            scoreboard.game_over()
            game_is_on = False
            print("Collision! Game Over")

    # Check if the player reached the end Y
    if player.check_reached_end():
        scoreboard.level += 1
        scoreboard.update_level()
        for c in cars:
            c.level_up()

    time.sleep(0.1)
    screen.update()
    num_of_loops += 1


screen.exitonclick()
