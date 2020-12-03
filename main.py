from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

is_on = True
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

screen.tracer(0)
screen.listen()

paddle1 = Paddle((370, 0))
paddle2 = Paddle((-370, 0))
ball = Ball()
score1 = Scoreboard((30, 250))
score2 = Scoreboard((-30, 250))

screen.onkey(paddle1.go_up, "Up")
screen.onkey(paddle1.go_down, "Down")
screen.onkey(paddle2.go_up, "w")
screen.onkey(paddle2.go_down, "s")

while is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()
    if ball.xcor() > 350:
        if paddle1.new_y + 50 > ball.ycor() > paddle1.new_y-50:
            ball.bounce_x()

        else:
            ball.reset_position()
            score2.point()

    elif ball.xcor() < -350:
        if paddle2.new_y + 50 > ball.ycor() > paddle2.new_y-50:
            ball.bounce_x()
        else:
            ball.reset_position()
            score1.point()

screen.exitonclick()
