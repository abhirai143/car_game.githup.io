from turtle import Turtle
import random

COLOR = ["red", "orange", "yellow", "black", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManger:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_time = random.randint(1, 6)
        if random_time == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLOR))
            new_car.penup()
            new_y = random.randint(-250, 250)
            new_car.goto(300, new_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT


