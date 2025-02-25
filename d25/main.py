import turtle
import pandas

data = pandas.read_csv("50_states.csv")
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

t = turtle.Turtle()
t.hideturtle()
t.penup()

guessed_states = []
states_list = data.state.to_list()

answer = screen.textinput(title=f"{len(guessed_states)}/50 States Guessed", prompt="Name a State").title()

while len(guessed_states) < 50:
        
    if answer in states_list:
        if answer not in guessed_states:
            guessed_states.append(answer)
            check_answer = data[data.state == answer]
            x_axis, y_axis = int(check_answer.x), int(check_answer.y)
            t.goto(x_axis, y_axis)
            t.write(f"{answer}")
            answer = screen.textinput(title=f"{len(guessed_states)}/50 States Guessed", prompt="Name a State").title()
        else:
            answer = screen.textinput(title=f"{len(guessed_states)}/50 States Guessed", prompt="You've already guessed that state. Try again.").title()
    else:
        answer = screen.textinput(title=f"{len(guessed_states)}/50 States Guessed", prompt="State not found. Try again.").title()

if len(guessed_states) == 50:
    print("You've guessed all 50 states!")
    screen.bye()

missing_states = []
for state in states_list:
    if state not in guessed_states:
        missing_states.append(state)
new_data = pandas.DataFrame(missing_states)
new_data.to_csv("states_to_learn.csv")
