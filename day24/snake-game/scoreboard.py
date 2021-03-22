from turtle import Turtle
import os


ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
LOCATION = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
FILENAME = "data.txt"
FULL_PATH = os.path.join(LOCATION, FILENAME)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open(FULL_PATH) as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(os.path.join(LOCATION, FILENAME), mode="w") as file:
                file.write(str(self.high_score))
            
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
