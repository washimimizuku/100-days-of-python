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
screen.onkey(player.move, "Up")

game_is_on = True
counter = 0
level = 0
while game_is_on:
    time.sleep(0.1)
    if counter % 6 == 0:
        car_manager.add_car(level)
    car_manager.move_all_cars()
    counter += 1
    screen.update()

    # Detect collision with car
    if car_manager.detect_collision(player):
        scoreboard.game_over()
        game_is_on = False

    # Detect reaching finish line
    if player.detect_win():
        level += 1
        player.reset_position()
        car_manager.new_level(level)
        scoreboard.new_level()

screen.exitonclick()