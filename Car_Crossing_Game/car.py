from turtle import Turtle
import random
COLORS = ["orange","red","violet","purple","blue","cyan","green","brown","gray","skyblue","maroon","lightgreen","darkgreen","turquoise"]

class Car(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(300,0)
        self.all_cars = []
        self.speed = 5
        
    def new_car(self):
        new_car = Turtle("square")
        new_car.shapesize(1,2)
        new_car.penup() 
        new_car.color(random.choice(COLORS))
        random_y = random.randint(-240,240)
        new_car.goto(300,random_y)
        self.all_cars.append(new_car)
        
    def move_car(self):
        for car in self.all_cars:
            car.backward(self.speed)
        
    def speed_up(self):
        self.speed += 1