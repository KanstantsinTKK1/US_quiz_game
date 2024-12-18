import turtle
from turtle import Screen
import pandas
from write_state import WriteState

screen = Screen()
screen.setup(width=725, height=491)
screen.title('U.S. Quiz Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
quiz_is_on = True
data_states = pandas.read_csv("50_states.csv")
states = data_states.state.to_list()
print(states)
write_name = WriteState()
right_state = 0

while quiz_is_on:
    user_answer = screen.textinput(title=f"{right_state}/50 States Correct", prompt="What's another state's name?")
    for state in states:
        if user_answer.title() == state:
            position_x = data_states[data_states.state == state].x.item()
            print(position_x)
            position_y = int(data_states.loc[data_states.state == state, 'y'].iloc[0])
            print(position_y)
            write_name.move_and_write(state, position_x, position_y)
            right_state += 1
            states.remove(state)
            print(states)
    if right_state == 50:
        quiz_is_on = False
    if user_answer == 'exit':
        quiz_is_on = False
        miss_states_csv = pandas.DataFrame(states)
        print(miss_states_csv)
        miss_states_csv.to_csv("miss_states.csv")


screen.exitonclick()


