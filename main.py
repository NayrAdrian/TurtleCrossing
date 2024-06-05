import time
import random
from turtle import Screen
from player import Player
from car_fleet import CarFleet
from scoreboard import Scoreboard
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_fleet = CarFleet()


screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_fleet.move_cars()
    car_fleet.remove_off_screen_cars()
    if random.randint(1, 6) == 1:
        car_fleet.spawn_car()
    screen.update()

    # Detect collision with cars
    for car in car_fleet.cars:
        if player.distance(car) < 21:
            print("Collision detected!")
            game_is_on = False

    # Detect collision with finish line
    if player.ycor() > 280:
        print("Next Round!")
        player.reset_position()
        scoreboard.next_round()

screen.exitonclick()
