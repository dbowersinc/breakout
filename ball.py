from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        x_start = random.randint(-200, 200)
        y_start = random.randint(-200, 0)
        self.speed_level = 0
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 3
        self.y_move = 3
        self.move_speed = 1.01
        self.starting_position = (x_start, y_start)
        self.goto(self.starting_position)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def update_speed(self, speed):
        self.speed_level += speed
        self.move_speed += self.speed_level * 0.01
        self.increase_speed()

    def increase_speed(self):
        self.x_move *= self.move_speed
        self.y_move *= self.move_speed
        print(f'speed increased to {self.x_move}')

    def reset_position(self):
        self.goto(self.starting_position)
        self.x_move = 3
        self.y_move = 3
        self.move()
