from turtle import  Screen
from paddle import Paddle
from ball import Ball
import time

is_on = True
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

screen.tracer(0)
screen.listen()

paddle1 = Paddle((350,0))
paddle2 = Paddle((-350, 0))
ball = Ball()


screen.onkey(paddle1.go_up, "Up")
screen.onkey(paddle1.go_down, "Down")
screen.onkey(paddle2.go_up,"w")
screen.onkey(paddle2.go_down, "s")



while is_on:
    screen.update()
    ball.move()
    time.sleep(0.05)





























screen.exitonclick()
