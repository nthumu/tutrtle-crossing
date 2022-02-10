from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def player_move(self):
        new_y = self.ycor() + 10
        self.goto(0, new_y)

    def player_start(self):
        self.goto(STARTING_POSITION)

