from turtle import Turtle
import random

MIN_AXIS = -270
MAX_AXIS = 270

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.random_goto()

    def random_goto(self):
        random_x = random.randint(MIN_AXIS, MAX_AXIS)
        random_y = random.randint(MIN_AXIS, MAX_AXIS)
        self.goto(random_x, random_y)
    
    def refresh(self):
        self.random_goto()