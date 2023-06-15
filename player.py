from turtle import Turtle

STARTING_POSITION = (0, -290)
MOVE_DISTANCE = 5
FINISH_Y_LINE = 280

class Car(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.reset_level()

    def up(self):
        self.forward(MOVE_DISTANCE)

    def reset_level(self):
        self.goto(STARTING_POSITION)

    def detect_finish(self):
        if self.ycor() > FINISH_Y_LINE:
            return True
        else:
            return False
