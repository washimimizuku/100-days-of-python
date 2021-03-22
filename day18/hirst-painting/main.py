import colorgram
import turtle as t
import random
import os


LOCATION = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
FILENAME = "hilda.jpeg"
FULL_PATH = os.path.join(LOCATION, FILENAME)


rgb_colors = []
colors = colorgram.extract(FULL_PATH, 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)

t.colormode(255) 
timmy = t.Turtle()
timmy.speed("fastest")
timmy.hideturtle()


def draw_square_dots(number_per_side, spacing, size):
    timmy.pensize(size)
    timmy.penup()

    timmy.setheading(225)
    timmy.forward(spacing + spacing * number_per_side / 2)

    timmy.setheading(0)

    for _ in range(number_per_side):
        for _ in range(number_per_side):
            timmy.color(random.choice(rgb_colors))
            timmy.dot()
            timmy.forward(spacing)
        timmy.left(90)
        timmy.forward(spacing)
        timmy.left(90)
        timmy.forward(spacing * number_per_side)
        timmy.setheading(0)

draw_square_dots(10, 50, 10)

screen = t.Screen()
screen.exitonclick()