import colorgram
import turtle as t
import random
# rgbc=[]
# color=colorgram.extract('image.jpg',30)
# for c in color:
#     r = c.rgb.r
#     g = c.rgb.r
#     b = c.rgb.r
#     n_c=(r,g,b)
#     rgbc.append(n_c)
# print(rgbc)

tim=t.Turtle()
t.colormode(255)
color_li=[(253, 253, 253), (235, 235, 235), (198, 198, 198), (248, 248, 248), (40, 40, 40), (244, 244, 244), (39, 39, 39), (238, 238, 238), (227, 227, 227), (29, 29, 29), (212, 212, 212), (17, 17, 17), (241, 241, 241), (195, 195, 195), (223, 223, 223), (68, 68, 68), (61, 61, 61), (223, 223, 223), (11, 11, 11), (219, 219, 219), (54, 54, 54), (19, 19, 19), (238, 238, 238), (79, 79, 79), (10, 10, 10), (73, 73, 73), (93, 93, 93), (65, 65, 65), (217, 217, 217)]
tim.speed("fastest")
tim.penup()
tim.ht()
tim.setheading(225)
tim.forward(250)
tim.setheading(0)
num_dots=100
for _ in range(1,num_dots+1):
    tim.dot(20,random.choice(color_li))
    tim.forward(50)
    if _ %10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)




screen=t.Screen()
screen.exitonclick()





