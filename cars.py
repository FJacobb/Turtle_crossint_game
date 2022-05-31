from turtle import Turtle
import random


class Cars(Turtle):

    def __init__(self):
        super().__init__()
        self.cars_list = []
        self.cars_start()
        self.y = 0
        self.x = 0
        self.color = (0, 0, 0)
        self.Speed = 10

    def cars_start(self):
        for i in range(20):
            self.car()

    def refresh_car(self, car):
        self.random_y()
        car.goto(x=290, y=self.y)

    def car(self):
        self.color_gen()
        self.random_x()
        self.random_y()
        new = Turtle(shape="square")
        new.penup()
        new.setheading(180)
        new.color(self.color)
        new.shapesize(stretch_len=1.5)
        new.goto(x=self.x, y=self.y)
        self.cars_list.append(new)

    def car_movemet(self):
        for turtle_car in self.cars_list:
            turtle_car.forward(self.Speed)

    def random_y(self):
        self.y = random.randint(-250, 280)

    def random_x(self):
        self.x = random.randint(-300, 300)

    def color_gen(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        self.color = (r, g, b)

    def car_speed(self):
        self.Speed += 5

