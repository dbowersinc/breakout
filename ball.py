from turtle import Turtle
import random

BASE_MOVE_DISTANCE = 5

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        x_start = random.randint(-200, 200)
        y_start = random.randint(-200, 0)
        self.speed_level = 0
        self.color("white")
        self.shape("circle")
        self.penup()
        self.move_distance = BASE_MOVE_DISTANCE
        self.setheading(45)
        self.max_speed = 10
        self.starting_position = (x_start, y_start)
        self.goto(self.starting_position)

    def move(self):
        self.forward(self.move_distance)

    def bounce_y(self):
        current_heading = self.heading()
        print(current_heading)
        if 90 < current_heading < 180:
            new_heading = current_heading + 90
        elif 180 < current_heading < 270:
            new_heading = current_heading - 90
        elif 0 < current_heading < 90:
            new_heading = current_heading + 270
        elif 270 < current_heading < 360:
            new_heading = current_heading - 270
        else:
            new_heading = 45

        self.setheading(new_heading)

    def bounce_x(self):
        current_heading = self.heading()
        if 90 < current_heading < 180 or 270 < current_heading < 360:
            new_heading = current_heading - 90
        elif 0 < current_heading < 90 or 180 < current_heading < 270:
            new_heading = current_heading + 90
        else:
            new_heading = 45
        self.setheading(new_heading)

    def increase_speed(self, speed):
        if self.move_distance < self.max_speed:
            self.move_distance = BASE_MOVE_DISTANCE + speed

    def reset_position(self):
        self.goto(self.starting_position)
        self.setheading(315)
        self.move()
