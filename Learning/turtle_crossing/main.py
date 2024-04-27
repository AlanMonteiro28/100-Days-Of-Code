from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Turtle Crossing Capstone")
screen.bgcolor("black")
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = ScoreBoard()
cars.create_initial_cars() #cria 15 carros inicialmente para a tela nao ficar quase toda vazia quando começa

screen.listen()
# setas
screen.onkeypress(player.move_up, "Up")
screen.onkeypress(player.move_down, "Down")
screen.onkeypress(player.move_left, "Left")
screen.onkeypress(player.move_right, "Right")
# w a s d
screen.onkeypress(player.move_up, "w")
screen.onkeypress(player.move_down, "s")
screen.onkeypress(player.move_left, "a")
screen.onkeypress(player.move_right, "d")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_cars()

    # detecta colisão
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # detecta se chegou no final
    if player.ycor() > 280:
        player.go_to_start()
        cars.level_up()
        scoreboard.increase_score()



screen.exitonclick()
