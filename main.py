import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    # Detect collisions with car
    for cars in car_manager.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect collisions with top-edge
    if player.ycor() > 280:
        player.go_to_start()
        car_manager.inc_speed()
        scoreboard.increase_level()


screen.exitonclick()
