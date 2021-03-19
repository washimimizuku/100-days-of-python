from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "cyan", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Car(Turtle):
    def __init__(self, level):
        super().__init__()
        self.shape("square")
        self.color(choice(COLORS))
        self.setheading(180)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(300, randint(-250, 250))
        self.car_speed = STARTING_MOVE_DISTANCE + level * MOVE_INCREMENT

    def move(self):
        self.forward(self.car_speed)
    
    def increase_speed(self, level):
        self.car_speed = STARTING_MOVE_DISTANCE + level * MOVE_INCREMENT
