from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier",24,"normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        with open("high_score.txt") as data:
            self.highscore = int(data.read())
        self.penup()
        self.goto(0,270)
        self.write(f"Score: {self.score} HighScore: {self.highscore}", align="center", font=("Arial",24,"normal"))
        self.hideturtle()
        
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} HighScore: {self.highscore}", align= ALIGNMENT, font=FONT)
        
    def increase_score(self):
        self.score += 1
        self.update_score()
        
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("high_score.txt",mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_score()
        
    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER😔", align=ALIGNMENT, font=FONT)
        