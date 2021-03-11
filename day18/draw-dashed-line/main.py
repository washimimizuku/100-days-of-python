from turtle import Turtle

timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")

for _ in range(15):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()
