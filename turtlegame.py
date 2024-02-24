from turtle import Turtle,Screen
import random
t=Turtle()
t.hideturtle()
s=Screen()
s.setup(width=500,height=500)
user_bet=s.textinput(title="Make your bet",prompt="Which turtle will win the race?Enter a color :")
colors=["red","orange","yellow","green","blue","purple"]
y_p=[-70,-40,-10,20,50,80]
turtle_list=[]
for i in range(0,6):
    ts=Turtle(shape="turtle")
    ts.penup()
    ts.color(colors[i])
    ts.goto(x=-230,y=y_p[i])
    turtle_list.append(ts)
if user_bet:
    is_race_on=True
while is_race_on:
    for i in turtle_list:
        if i.xcor()>230:
            is_race_on=False
            winnning_color=i.pencolor()
            if user_bet==winnning_color:
                print(f"You've won! The {winnning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winnning_color} tutle is the winner!")
        k=random.randint(0,10)
        i.forward(k)
s.exitonclick()