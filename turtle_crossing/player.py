from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green4")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        if self.ycor() > -280:
            self.backward(MOVE_DISTANCE)

    def move_left(self):
        if self.xcor() > -380:
            self.setx(self.xcor() - MOVE_DISTANCE)

    def move_right(self):
        if self.xcor() < 380:
            self.setx(self.xcor() + MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)
