from car_manager import CarManager
import random

class CarFleet:
    def __init__(self):
        self.cars = []
        self.spawn_car()

    def spawn_car(self):
        new_car = CarManager()
        self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.car_move()

    def remove_off_screen_cars(self):
        self.cars = [car for car in self.cars if car.xcor() > -320]
