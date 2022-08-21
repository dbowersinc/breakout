from turtle import Turtle

# TODO add lives and test for lives remaining

class Scoreboard(Turtle):

    def __init__(self, sidewall, top):
        super().__init__()
        self.sidewall = sidewall
        self.top_line = top
        self.score_position = (self.sidewall - 100, self.top_line)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.draw_top_line()
        self.goto(self.score_position)
        self.write(self.score, align="center", font=("Courier", 80, "normal"))

    def update_points(self, value):
        self.score += value
        self.update_scoreboard()

    def draw_top_line(self):
        self.goto(-self.sidewall, self.top_line)
        self.pendown()
        self.goto(self.sidewall, self.top_line)
        self.penup()
