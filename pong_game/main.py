from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Arcade Game")
screen.tracer(0)

paddle_1 = Paddle((-350, 0))
paddle_2 = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()


def update_key_binding():
    if paddle_1.ycor() > 240:
        screen.onkeypress(lambda: None, "w")
    else:
        screen.onkeypress(paddle_1.go_up, "w")
    if paddle_1.ycor() < -230:
        screen.onkeypress(lambda: None, "s")
    else:
        screen.onkeypress(paddle_1.go_down, "s")
    if paddle_2.ycor() > 240:
        screen.onkeypress(lambda: None, "Up")
    else:
        screen.onkeypress(paddle_2.go_up, "Up")
    if paddle_2.ycor() < -230:
        screen.onkeypress(lambda: None, "Down")
    else:
        screen.onkeypress(paddle_2.go_down, "Down")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    # verifica se paddle chegou no ponto maximo e minimo
    update_key_binding()

    # colisão com parede
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # colisão com o paddle
    if ball.xcor() > 325 and ball.distance(paddle_2) < 50 or ball.xcor() < -325 and ball.distance(paddle_1) < 50:
        ball.bounce_x()

    # não teve colisão e a bola passou do paddle
    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.p1_point()

    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.p2_point()

screen.mainloop()
