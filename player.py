from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    # Create a turtle when initializing.
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    # Moves turtle forward a certain distance.
    def move(self):
        self.forward(MOVE_DISTANCE)

    # Reset to starting pos when player reaches finish line.
    def reset_pos(self):
        self.goto(STARTING_POSITION)
