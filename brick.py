from turtle import Turtle


class Brick(Turtle):

    def __init__(self, color, value, position):
        super().__init__()
        self.color(color)
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.penup()
        self.value = value
        self.goto(position)

