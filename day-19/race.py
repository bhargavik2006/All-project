from turtle import  Turtle,Screen
import random
is_race_on=False

screen=Screen()
screen.setup(500,400)
user_bet=screen.textinput(title="Make you Bet",prompt="which turtle win the race? Enter the color:")
colors=["red","orange","yellow","green","blue","purple"]
y_positions=[-70,-40,-10,20,50,80]
all_turtle=[]
print(user_bet)
for turtle_index in range(0,6):

    new_tutle=Turtle(shape="turtle")
    new_tutle.color(colors[turtle_index])
    new_tutle.penup()
    new_tutle.goto(x=-230,y=-y_positions[turtle_index])
    all_turtle.append(new_tutle)
if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor()>230:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print(f"u won! the {winning_color} turtle is winner!")
            else:
                print(f"u lost! the {winning_color} turtle is winner!")

        random_distance=random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()
