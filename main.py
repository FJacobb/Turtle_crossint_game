from turtle import Screen
from score import Score
from cars import Cars
from player_turtle import Playerturtle
import time
from gameover import Gameover
screen = Screen()
screen.colormode(255)
screen.title("Turtle Crossing")
screen.bgcolor("black")
screen.setup(600, 600)
screen.listen()
screen.tracer(0)
score_line = Score()
Game = Gameover()
car = Cars()

player = Playerturtle()
screen.onkeypress(key="Up", fun=player.up1)
speed = 0.2
game_on = True
while game_on:
    time.sleep(speed)
    car.car_movemet()
    if player.turtle_list[0].ycor() > 290:
        player.refresh_player()
        score_line.refresh_score()
        car.car_speed()
    for x in range(0, len(car.cars_list)):
        if player.turtle_list[0].distance(car.cars_list[x]) < 24:
            Game.print()
            score_line.save_score()
            game_on = False
        if car.cars_list[x].xcor() < -290:
            car.refresh_car(car.cars_list[x])
    screen.update()

screen.exitonclick()
