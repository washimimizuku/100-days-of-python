import turtle
import pandas
import os


LOCATION = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
FILENAME_STATES = "50_states.csv"
FILENAME_BACKGROUND = "blank_states_img.gif"
FILENAME_STATES_TO_LEARN = "states_to_learn.csv"
FULL_PATH_STATES = os.path.join(LOCATION, FILENAME_STATES)
FULL_PATH_BACKGROUND = os.path.join(LOCATION, FILENAME_BACKGROUND)
FULL_PATH_STATES_TO_LEARN = os.path.join(LOCATION, FILENAME_STATES_TO_LEARN)


screen = turtle.Screen()
screen.title("U.S. States Game")

screen.addshape(FULL_PATH_BACKGROUND)
turtle.shape(FULL_PATH_BACKGROUND)

states_data = pandas.read_csv(FULL_PATH_STATES)
us_states = states_data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?")
    answer_state = answer_state.title()
    
    if answer_state == "Exit":
        missing_states = []
        for state in us_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv(FULL_PATH_STATES_TO_LEARN)
        break
    
    if answer_state in us_states:
        guessed_states.append(answer_state)
        state_name = turtle.Turtle()
        state_name.hideturtle()
        state_name.penup()
        state_data = states_data[states_data.state == answer_state]
        state_name.goto(int(state_data.x), int(state_data.y))
        state_name.write(answer_state)
