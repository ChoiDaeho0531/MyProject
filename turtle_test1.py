#http://www.openbookproject.net/thinkcs/archive/python/thinkcspy3e_abandoned/ch04.html


import turtle


def draw_square(t, size):
    
    for i in range(4):
        t.forward(size)
        t.left(90)

turtle.setup(800, 600)
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("최대호")

TT = turtle.Turtle()

draw_square(TT, 250)

wn.exitonclick()
