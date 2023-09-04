from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        y_pos = random.randint(-250, 250)
        self.setposition((300, y_pos))
        self.setheading(180)  # 0
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.distance = STARTING_MOVE_DISTANCE

    def move(self):
        self.forward(self.distance)

    def level_up(self):
        self.distance = STARTING_MOVE_DISTANCE + MOVE_INCREMENT

    def set_speed(self, speed):
        self.distance = speed
