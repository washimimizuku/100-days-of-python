import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from random import randint

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    if randint(1, 6) == 1:
        car_manager.add_car()
    car_manager.move_all_cars()
    screen.update()

    # Detect collision with car
    if car_manager.detect_collision(player):
        scoreboard.game_over()
        game_is_on = False

    # Detect reaching finish line
    if player.detect_win():
        player.reset_position()
        car_manager.new_level()
        scoreboard.new_level()

screen.exitonclick()