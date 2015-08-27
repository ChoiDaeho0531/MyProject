__author__ = 'Daeho'

#https://www.youtube.com/watch?v=5oFFnvQfbXM

import turtle as t


def main():
    t.reset()
    t.down()
    t.speed(22)
    a = 1
    for i in range(1000):
        if a > 0:
            t.pencolor("red")
            a -= 2
        else:
            t.pencolor("blue") 
            a += 2
        t.forward(i)
        t.right(98)


main()
t.done()
