#http://www.openbookproject.net/thinkcs/archive/python/thinkcspy3e_abandoned/ch04.html

import turtle

def draw_multicolor_square(t, sz):
   
    for c in ['red', 'purple', 'hotpink', 'blue']:
        t.color(c)
        t.forward(sz)
        t.left(90)


turtle.setup(800, 600)
wn = turtle.Screen()
wn.bgcolor("skyblue")
wn.title("최대호")


TT = turtle.Turtle()
TT.pensize(3)

size = 20                        
for i in range(25):
    draw_multicolor_square(TT, size)
    size = size + 10            
    TT.forward(10)            
    TT.right(18)
    
wn.exitonclick()
