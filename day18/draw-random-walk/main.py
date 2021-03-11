import turtle as t
import random

t.colormode(255) 
timmy = t.Turtle()
timmy.shape("turtle")

timmy.pensize(15)
timmy.speed(10)

angles = [0, 90, 180, 270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color = (r, g, b)
    return color

def draw_random_walk():
    timmy.color(random_color())
    angle = random.choice(angles)
    
    timmy.setheading(angle)
    timmy.forward(30)

for _ in range(200):
    draw_random_walk()
