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
car_manager = CarManager


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
            scoreboard.game_over()
            game_is_on = False

    # Detect collision with finish line
    if player.ycor() > 280:
        print("Next Round!")
        player.reset_position()
        car_fleet.increase_speed()
        scoreboard.next_level()

screen.exitonclick()
