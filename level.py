from turtle import Turtle


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.color()
        self.penup()
        self.level = 1
        self.hideturtle()
        self.displayLevel()


    def displayLevel(self):
        self.clear()
        self.goto(-250, 250)
        self.write(f"Level: {self.level}", align="left", font=("Courier", 24 , "normal"))

    def levelUpdate(self):
        self.level += 1
        self.displayLevel()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=("Courier", 24 , "normal"))
