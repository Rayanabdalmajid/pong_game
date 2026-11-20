from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

print(ball.heading())

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() == 280 or ball.ycor() == -280:
        ball.bounce()

    if (ball.distance(r_paddle) < 40 and ball.xcor() > 260) or (ball.distance(l_paddle) < 40 and ball.xcor() < -260):
        ball.bounce_of_paddle()
        ball.move_speed *= 0.9

    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.increase_l()
    elif ball.xcor() < -400:
        ball.reset_position()
        scoreboard.increase_r()





screen.exitonclick()