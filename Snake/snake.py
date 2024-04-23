from turtle import Turtle
import time
move_dist=20
Up,Down,Left,Right=90,270,180,0

SEG=[(0,0),(-20,0),(-40,0)]
class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]
    def create_snake(self):
        for pos in SEG:
            se=Turtle('square')
            se.color("white")
            se.penup()
            se.goto(pos)
            self.segments.append(se)
    def move(self):
        for seg in range(len(self.segments)-1,0,-1):
            x_cor=self.segments[seg-1].xcor()
            y_cor=self.segments[seg-1].ycor()
            self.segments[seg].goto(x_cor,y_cor)
        self.segments[0].forward(move_dist)
    def up(self):
        if self.head.heading()!=Down:
            self.head.setheading(Up)
    def down(self):
        if self.head.heading()!=Up:
            self.head.setheading(Down)    
    def left(self):
        if self.head.heading()!=Right:
            self.head.setheading(Left)   
    def right(self):
        if self.head.heading()!=Left:
            self.head.setheading(Right)

    
        

