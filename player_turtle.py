from turtle import Turtle


class Playerturtle:
    def __init__(self):
        self.turtle_list = []
        self.y_cor = -280
        self.player()

    def player(self):
        turtle = Turtle(shape="turtle")
        turtle.penup()
        turtle.color("white")
        turtle.setheading(90)
        turtle.goto(x=0, y=self.y_cor)
        self.turtle_list.append(turtle)

    def up1(self):
        self.turtle_list[0].goto(x=0, y=self.y_cor)
        self.y_cor += 10

    def refresh_player(self):
        self.y_cor = -280
        self.turtle_list[0].goto(x=0, y=self.y_cor)

