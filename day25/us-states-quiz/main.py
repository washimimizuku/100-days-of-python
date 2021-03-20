import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image_file = "blank_states_img.gif"
screen.addshape(image_file)

turtle.shape(image_file)

states_data = pandas.read_csv("50_states.csv")
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
        new_data.to_csv("states_to_learn.csv")
        break
    
    if answer_state in us_states:
        guessed_states.append(answer_state)
        state_name = turtle.Turtle()
        state_name.hideturtle()
        state_name.penup()
        state_data = states_data[states_data.state == answer_state]
        state_name.goto(int(state_data.x), int(state_data.y))
        state_name.write(answer_state)
