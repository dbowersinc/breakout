from turtle import Turtle

# TODO change paddle to go from left to right.
# TODO Paddle will grow and shrink depending on level.

class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.paddle_width = 8
        self.shapesize(stretch_wid=1, stretch_len=self.paddle_width)
        self.penup()
        self.goto(position)

    def go_left(self):
        new_x = self.xcor() - 60
        self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 60
        self.goto(new_x, self.ycor())

    def paddle_shrink(self):
        self.paddle_width = 4

    def paddle_reset(self):
        self.paddle_width = 8
