from turtle import Turtle

FONT = ("Courier", 24, "normal")
GAME_OVER_FONT = ("Courier", 24, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.player_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-300, 250)
        self.write(f"Level: {self.player_score}", align="center", font=FONT)

    def increase_score(self):
        self.player_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=GAME_OVER_FONT)
