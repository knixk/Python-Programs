from turtle import Turtle as t, Screen as s
import math
from random import choice, randint

colors = ["#E0FFFF", "red", "blue", "green", "purple", "cyan", "black"]

my_screen = s()
tt = t()


def draw_square():
    for i in range(0, 5):
        tt.fd(100)
        tt.rt(90)

# tt.color('#E0FFFF')
# draw_square()

def create_dashed_line():
    for _ in range(10):
        tt.pd()
        tt.forward(10)
        tt.pu()
        tt.forward(10)

def draw_polygon(n):
    # tt.setposition(10, 10)
    sides = n
    angle = math.floor(360 / sides)

    for _ in range(sides):
        tt.fd(100)
        tt.rt(angle)

# create_dashed_line()    
# draw_polygon(10)

# for i in range (3, 11):
    random_color = choice(colors)
    tt.color(random_color)
    draw_polygon(i)

def random_walk(steps):
        
    tt.pensize(10)
    
    for _ in range(steps):
        color = choice(colors)
        tt.color(color)
        angle = randint(0, 361) 
        distance = randint(0, 100)
        tt.fd(distance)
        tt.right(angle)


# random_walk(100)

my_screen.exitonclick()

# so far we have the code for random walk..