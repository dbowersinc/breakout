from turtle import Screen, Turtle

import wall
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from brick import Brick
from wall import Wall
import time

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
BRICKS_PER_ROW = 13
BRICK_ROWS = 8

sidewalls = int(SCREEN_WIDTH/2)
top_line = int(SCREEN_HEIGHT/2) - 100
paddle_line = -int(SCREEN_HEIGHT/2) + 20
print(sidewalls)

screen = Screen()
screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Breakout")
screen.tracer(0)

b_paddle = Paddle((0, paddle_line))
ball = Ball()
scoreboard = Scoreboard(sidewall=sidewalls, top=top_line)
wall = Wall(SCREEN_WIDTH)
wall.build_board()

screen.listen()
screen.onkey(b_paddle.go_left, "Left")
screen.onkey(b_paddle.go_right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    # Detect collision with brick
    for brick in wall.bricks:
        if ball.distance(brick) < 40 and ball.ycor() > 0:
            print(f"Brick hit @ {ball.position()}")
            scoreboard.update_points(value=brick.value)
            scoreboard.update_session(1)
            wall.destroy_brick(wall.bricks.index(brick))
            if wall.all_bricks_destroyed():
                print("Wall Destroyed!")
                game_is_on = False
            # Speed increases after every 4 blocks are destroyed.
            if scoreboard.session >= 4:
                new_speed = int(scoreboard.session/4)
                ball.increase_speed(new_speed)

            ball.bounce_y()

    # Detect broke top layer
    if ball.ycor() > 155:
        b_paddle.paddle_shrink()

    # Detect collision with paddle
    if ball.distance(b_paddle) < 60 and ball.ycor() <= paddle_line + 15:
        print(f"Paddle hit @ {ball.position()}")
        ball.bounce_y()

    # Detect collision with sidewalls
    if ball.xcor() > sidewalls or ball.xcor() < -sidewalls:
        print(f"Sidewalls hit @ {ball.position()}: {ball.heading()}")
        ball.bounce_x()

    # Detect collision with top_line
    if ball.ycor() > top_line:
        ball.bounce_y()

    # Detect collision with bottom - lose turn, game is off.
    if ball.ycor() < paddle_line:
        print(f"Missed paddle {ball.position()}, Paddle position @ {b_paddle.position()}")
        scoreboard.reset_session()
        ball.reset_position()

    time.sleep(.01)


screen.exitonclick()