from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x, y)

    def go_up(self):
        if self.ycor() < 250:  # Add boundary check
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() > -250:  # Add boundary check
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
    
    def reset_position(self, x):
        self.goto(x, 0)