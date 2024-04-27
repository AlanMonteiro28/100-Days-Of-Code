from turtle import Turtle
import random

COLORS = ["goldenrod2", "gray", "magenta4", "DodgerBlue4", "orange", "red3"]
STARTING_MOVE_DISTANCE = 5


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.create_initial_cars()

    def create_initial_cars(self):
        for _ in range(15):
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2.5)
            new_car.color(random.choice(COLORS))
            x_cor = random.randint(-300, 300)
            y_cor = random.randint(-250, 240)
            new_car.penup()
            new_car.goto(x_cor, y_cor)
            self.all_cars.append(new_car)

    def create_car(self):
        random_create = random.randint(1, 4)
        if random_create == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2.5)
            new_car.color(random.choice(COLORS))
            y_cor = random.randint(-250, 240)
            new_car.penup()
            new_car.goto(300, y_cor)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += self.car_speed/3
