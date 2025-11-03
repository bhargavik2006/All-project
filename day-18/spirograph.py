import turtle as t
import random
timmy=t.Turtle()
t.colormode(255)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)

    random_color=(r,g,b)
    return random_color
timmy.speed("fastest")
def draw_s(size):
    for _ in range(360//size):
        timmy.color(random_color())
        timmy.circle(100)
        current_heading=timmy.heading()
        timmy.setheading(current_heading+size)
draw_s(5)
screen=t.Screen()
screen.exitonclick()