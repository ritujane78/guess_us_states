# import turtle
from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
tim = Turtle()
tim.shape(image)
data = pandas.read_csv("50_states.csv")


def write_state_name(state):
    text = Turtle()
    text.penup()
    text.hideturtle()
    text.goto(data[data.state == state].x.to_list()[0], data[data.state == state].y.to_list()[0])
    text.color('black')
    text.write(f"{state}", False, 'center', ('courier', 14, 'normal'))


guessed_states = []

while len(guessed_states) < 50:
    user_answer = screen.textinput(title=f"{len(guessed_states)}/{len(data)} states guessed", prompt="Enter a state's name")
    states = data["state"].to_list()

    if user_answer.lower() == "exit":
        missed_states = [state for state in states if state not in guessed_states]
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("states_to_learn.csv")
        break

    for state in states:
        if state.lower() in user_answer.lower():
            guessed_states.append(state)
            write_state_name(state)
