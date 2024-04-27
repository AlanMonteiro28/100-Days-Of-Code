import turtle
import pandas

screen = turtle.Screen()
screen.title("BR States Game")
screen.setup(width=800, height=800)
image = "brazil_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("brazil_states.csv", delimiter=";")
counter = 0
guessed_states = []

#
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)

while len(guessed_states) < 27:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/26 States Correct", prompt="What's another name?").title()

    if answer_state == "Exit":
        all_states = data.state.to_list()
        missing_states = []
        for s in all_states:
            if s not in guessed_states:
                missing_states.append(s)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn")
        break

    for state in data.state:
        if answer_state.lower() == state.lower():
            t = turtle.Turtle(visible=False)
            x_position = data[data["state"] == state]["x"].values[0]
            y_position = data[data["state"] == state]["y"].values[0]

            t.clear()
            t.penup()
            t.goto(x_position, y_position)
            t.write(arg=answer_state, font=("Arial", 12, "bold"))

            guessed_states.append(answer_state)

