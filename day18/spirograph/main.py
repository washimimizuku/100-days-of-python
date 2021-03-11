import turtle as t
import random

t.colormode(255) 
timmy = t.Turtle()
timmy.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color = (r, g, b)
    return color

def draw_circle(angle, radius):
    timmy.color(random_color())
    timmy.setheading(angle)
    timmy.circle(radius)

def draw_spirograph(size_of_gap):
    angle = 0
    for _ in range(int(360 / size_of_gap)):
        draw_circle(angle, 100)
        angle += size_of_gap

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()