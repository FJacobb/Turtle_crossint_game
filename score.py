from turtle import Turtle

FONT = 10


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.high_score = 0
        self.score_of_user = 0
        self.save_score()
        self.color("white")
        self.penup()
        self.score()

    def score(self):
        self.goto(x=-270, y=270)
        self.write(f"Level {self.score_of_user}", font=("Algerian", FONT, "normal"))
        self.goto(x=180, y=270)
        self.write(f"High Level {self.high_score}", font=("Algerian", FONT, "normal"))

    def refresh_score(self):
        self.clear()
        self.score_of_user += 1
        self.score()
        self.save_score()

    def save_score(self):
        with open("Score.txt", mode="r") as file:
            self.high_score = int(file.read())

        if self.score_of_user > self.high_score:
            self.high_score = self.score_of_user
            with open("Score.txt", mode="w") as file:
                file.write(f"{self.high_score}")
