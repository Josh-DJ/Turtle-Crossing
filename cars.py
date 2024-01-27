import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Car:
    # Create empty list of Cars when initializing
    def __init__(self):
        super().__init__()
        self.cars = []

    # Create a singular Car to be added to cars list.
    def create(self):
        generate_chance = random.randint(1,6)
        if generate_chance == 1:
            new_car = Turtle("square")
            y_axis = random.randint(-250, 260)
            new_car.shapesize(stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(325, y_axis)
            self.cars.append(new_car)

    # Iterate through cars list and moves each car by distance amount.
    def move(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)
            if car.xcor() < -300:
                car.hideturtle()

    # Detects collision of car with player
    def collision(self, player):
        for car in self.cars:
            if player.distance(car) < 23:
                return True
        return False

    # Updates speed when new level is reached
    def inc_speed(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT

