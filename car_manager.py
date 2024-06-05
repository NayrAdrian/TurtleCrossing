from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self, speed=STARTING_MOVE_DISTANCE):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(300, random.randint(-250, 250))
        self.y_move = speed
        self.x_direction = -1

    def car_move(self):
        new_x = self.xcor() + self.x_direction * self.y_move
        self.goto(new_x, self.ycor())

    def increase_speed(self):
        self.y_move += MOVE_INCREMENT






