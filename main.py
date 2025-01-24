import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()

game_is_on = True
Correct_answers = []

while len(Correct_answers) < 50:
    answer_state = screen.textinput(title=f"{len(Correct_answers)}/50",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        States_to_learn = [state for state in states if state not in Correct_answers]
        new_data = pandas.DataFrame(States_to_learn).to_csv("States_To_Learn")
        break

    if answer_state in states:
        Correct = turtle.Turtle()
        Correct_answers.append(answer_state)
        Correct.hideturtle()
        Correct.up()
        state_data = data[data.state == answer_state]
        Correct.goto(int(state_data.x), int(state_data.y))
        Correct.write(answer_state)

