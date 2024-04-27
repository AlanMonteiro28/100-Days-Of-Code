import turtle
import random
is_race_on = False
width = 500
height = 400
start_x = -width/2+15
start_y = -height/2+100
spacing = 35
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

screen = turtle.Screen()
screen.setup(width, height)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
if user_bet:
    is_race_on = True

#armazenando cada objeto em uma lista e definindo qual será o ponto inicial de cada um desses objetos
turtle_list = []
for i in range(6):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.shapesize(1.2)
    new_turtle.color("black", colors[i])
    new_turtle.penup()
    turtle_list.append(new_turtle)
    if i == 0:
        turtle_list[i].goto(start_x, start_y)
    else:
        turtle_list[i].goto(start_x, start_y + spacing * i)

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 238:
            is_race_on = False
            winning_color = turtle.fillcolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            screen.bye()
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
