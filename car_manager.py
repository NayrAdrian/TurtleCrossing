from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(300, random.randint(-250, 250))
        self.x_move = STARTING_MOVE_DISTANCE
        self.x_direction = -1

    def car_move(self):
        new_x = self.xcor() + self.x_direction * self.x_move
        self.goto(new_x, self.ycor())






