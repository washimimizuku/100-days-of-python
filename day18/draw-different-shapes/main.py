from turtle import Turtle
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")

colors = ["red", "green", "yellow", "blue", "cyan", "magenta", "teal"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)

for shape_side_n in range(3, 11):
    timmy.color(random.choice(colors))
    draw_shape(shape_side_n)
