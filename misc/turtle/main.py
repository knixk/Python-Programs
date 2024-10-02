from turtle import Turtle as t, Screen as s
import math

my_screen = s()
tt = t()

tt.color('red')

def draw_square():
    for i in range(0, 5):
        tt.fd(100)
        tt.rt(90)

tt.color('red')
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

for i in range (3, 11):
    draw_polygon(i)

my_screen.exitonclick()
