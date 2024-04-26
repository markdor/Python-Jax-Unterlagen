# Beispielprogramm für das Buch "Python Challenge"
#
# Copyright 2020 by Michael Inden


import turtle


def drawfigure():
    turtle.speed(10)
    turtle.begin_fill()
    while True:
        turtle.forward(300)
        turtle.left(95)
        if abs(turtle.pos()) < 10:
            break
    turtle.end_fill()


screen = turtle.Screen()
screen.setworldcoordinates(-100, -100, 500, 500)

turtle.color('red', 'blue')
drawfigure()
screen.exitonclick()
