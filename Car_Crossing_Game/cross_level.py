from turtle import Turtle

class Cross_level(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 1
        self.color("black")
        self.goto(-240,260)
        self.update_level()
        self.hideturtle()
        
    def update_level(self):
        self.write(f"Level: {self.score}", align="center", font=("Lusitana",20,"normal"))
        
    def next_level(self):
        self.score += 1
        self.clear()
        self.update_level()
        
    def finish_game(self):
        self.goto(0,0)
        self.write("GAME OVER!", align="center", font=("Martel",24,"normal"))
        