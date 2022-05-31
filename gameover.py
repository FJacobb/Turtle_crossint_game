from turtle import Turtle
FONT = 20


class Gameover(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")

    def print(self):
        self.write("Game Over", align="center", font=("Algerian", FONT, "normal"))
