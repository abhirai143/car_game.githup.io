from turtle import Screen
from player import Car
import time
from level import Level
from car_manger import CarManger

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("white")
screen.tracer(0)
player = Car()
level = Level()
car = CarManger()


screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()

    # detect player collision with the car
    for cars in car.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False
            level.game_over()

    # successful  cross
    if player.detect_finish():
        player.reset_level()
        car.level_up()
        level.levelUpdate()
        level.levelUpdate()

screen.exitonclick()


