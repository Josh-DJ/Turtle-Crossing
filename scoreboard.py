from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    # Creates scoreboard.
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-290, 260)
        self.write("Level: ", font=FONT)
        self.goto(-180, 260)
        self.write(self.level, font=FONT)

    # Updates score when new level is reached.
    def update(self):
        self.clear()
        self.level += 1
        self.goto(-290, 260)
        self.write("Level: ", font=FONT)
        self.goto(-180, 260)
        self.write(self.level, font=FONT)


    #Game over screen.
    def game_over(self):
        self.goto(0, 0)
        self.write("Game over.", align="center", font=FONT)
