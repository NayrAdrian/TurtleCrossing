from turtle import Turtle
from car_manager import CarManager
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.round = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(x=-230, y=260)
        self.write(f"Round: {self.round}", align="center", font=FONT)

    def next_round(self):
        self.round += 1
        self.update_scoreboard()
