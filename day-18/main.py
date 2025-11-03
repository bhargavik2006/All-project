import turtle
from turtle import Turtle,Screen
import random
import turtle as t
# timmy=Turtle()
# timmy.shape("turtle")
# timmy.color("brown")
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)  # to draw square

# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown() # TO DRAW (- - - - - - - - ->)



# colors=["indigo","pink","green", "yellow","pale violet red","navy","light cyan"]
# def draw_shape(num_side):
#     for _ in range(num_side):
#         angle=360/num_side
#         timmy.forward(100)
#         timmy.right(angle)
# for shape_side_n in range(3,11):
#     timmy.color(random.choice(colors))
#     draw_shape(shape_side_n)

timmy=t.Turtle()
t.colormode(255)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)

    random_color=(r,g,b)
    return random_color


directions=[0,90,180, 270]
timmy.speed(0)
timmy.pensize(10)
for _ in range(200):
    timmy.color(random_color())

    timmy.forward(30)
    timmy.setheading(random.choice(directions))












screen=Screen()
screen.exitonclick()
# ********************  how to import  ***************
# import heroes
# import villains
# print(heroes.gen())












