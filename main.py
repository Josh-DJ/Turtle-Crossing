import time
from turtle import Screen

import player
from player import Player
from cars import Car
from scoreboard import Scoreboard

# Create screen
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("white")
screen.title("Turtle Crossing")
screen.tracer(0)

# Create classes
turtle = Player()
car = Car()
score = Scoreboard()

# Listen to keyboard inputs
screen.listen()
screen.onkeypress(key="Up", fun=turtle.move)

# Main game loop
game_on = True
while game_on:
    time.sleep(0.1)  # Sleep to create delay
    screen.update()  # Updates screen to refresh animations

    # Create and move cars
    car.create()
    car.move()

    # Player collision with car
    if car.collision(turtle):
        game_on = False
        score.game_over()

    # Detect if player reaches finish line.
    if turtle.ycor() == player.FINISH_LINE_Y:
        score.update()
        turtle.reset_pos()
        car.inc_speed()



screen.exitonclick()
