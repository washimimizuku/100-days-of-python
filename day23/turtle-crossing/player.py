from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("green")
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def reset_position(self):
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)
    
    def detect_win(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False