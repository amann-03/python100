import time
from turtle import Turtle,Screen
from turtle_cross import Cross_road
from car import Car
from cross_level import Cross_level

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("yellow")
screen.title("Road_Cross_Game")
screen.tracer(0)

turtle = Cross_road()
level = Cross_level()
generate_cars = Car()
generate_cars.new_car()

screen.listen()
screen.onkeypress(turtle.go_up,"Up")
screen.onkeypress(turtle.go_down,"Down")
    
time.sleep(0.1)
screen.update()

game_is_on = True
loop = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    if loop >= 4: 
        loop = 0
        generate_cars.new_car()

    generate_cars.move_car()
        
    if turtle.ycor() > 280:
        level.next_level()
        generate_cars.speed_up()
        turtle.restart()
        
    for cars in generate_cars.all_cars:  
        if turtle.distance(cars) < 25:
            game_is_on = False
            level.finish_game()

    for cars in generate_cars.all_cars:
        if cars.xcor() < -300:
            cars.hideturtle()
            generate_cars.all_cars.remove(cars)
    
    loop += 1
        
screen.exitonclick()