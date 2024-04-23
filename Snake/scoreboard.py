from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.updateScore()
    def updateScore(self):
        self.write(f"Score:{self.score}",align="center",font=("Arial",18,"normal"))
    def game_is_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align='center',font=("Arail",18,"normal"))
    def increase_score(self):
        self.score+=1
        self.clear()
        self.updateScore()

