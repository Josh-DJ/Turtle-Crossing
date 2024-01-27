import time
from turtle import Screen
from player import Player
from cars import Car

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("white")
screen.title("Turtle Crossing")
screen.tracer(0)

turtle = Player()
car = Car()
screen.listen()
screen.onkeypress(key="Up", fun=turtle.move)

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

    car.create()
    car.move()

screen.exitonclick()
