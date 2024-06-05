from car_manager import CarManager, STARTING_MOVE_DISTANCE, MOVE_INCREMENT


class CarFleet:
    def __init__(self):
        self.cars = []
        self.current_speed = STARTING_MOVE_DISTANCE
        self.spawn_car()

    def spawn_car(self):
        new_car = CarManager(self.current_speed)
        self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.car_move()

    def remove_off_screen_cars(self):
        self.cars = [car for car in self.cars if car.xcor() > -320]

    def increase_speed(self):
        self.current_speed += MOVE_INCREMENT
        for car in self.cars:
            car.increase_speed()
