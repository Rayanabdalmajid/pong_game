from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        # self.shapesize(0.5)
        self.penup()
        self.move_x = 10
        self.move_y = 10
        self.move_speed = 0.1


    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def bounce(self):
        self.move_y *= -1

    def bounce_of_paddle(self):
        self.move_x *= -1

    def reset_position(self):
        self.move_speed = 0.1
        self.home()
        self.bounce_of_paddle()

    def increase_speed(self):
        self.speed()




