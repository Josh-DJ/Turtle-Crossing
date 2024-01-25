from turtle import Screen
import time


screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.bgcolor("white")
screen.title("Turtle Crossing")






game_on = True
screen.exitonclick()

while game_on:
    time.sleep(0.1)
    screen.update()
