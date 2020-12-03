from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.paddle = Turtle()
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.pu()
        self.paddle.shapesize(stretch_wid=5, stretch_len= 1)
        self.paddle.goto(position)
        self.new_y = 0
        self.new_x = 0

    def go_up(self):
        self.new_y = self.paddle.ycor() + 40
        self.paddle.goto(self.paddle.xcor(), self.new_y)

    def go_down(self):
        self.new_y = self.paddle.ycor() - 40
        self.paddle.goto(self.paddle.xcor(), self.new_y)
