from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from score_pong import Scoreboard
import time

dashed = Turtle()
dashed.color("white")
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_pad = Paddle((350,0))
l_pad = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

dashed.setheading(90)
for _ in range(15):
    dashed.forward(10)
    dashed.penup()
    dashed.forward(10)
    dashed.pendown()

dashed.penup()
dashed.goto(0,0)

for _ in range(15):
    dashed.backward(10)
    dashed.penup()
    dashed.backward(10)
    dashed.pendown()
    
screen.listen()
screen.onkeypress(r_pad.go_up,"Up")
screen.onkeypress(r_pad.go_down,"Down")
screen.onkeypress(l_pad.go_up,"w")
screen.onkeypress(l_pad.go_down,"s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    # Detect collision with upper-wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    # detect collision with paddle
    if ball.distance(r_pad) < 40 and ball.xcor() > 320 or ball.distance(l_pad) < 40 and ball.xcor() < -320:
        ball.bounce_x()
        
    # detect when either paddle misses the ball
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()
        
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()

    if scoreboard.l_score == 5 or scoreboard.r_score == 5:
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()