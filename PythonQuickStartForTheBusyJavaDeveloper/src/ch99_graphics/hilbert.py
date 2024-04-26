# Beispielprogramm für das Buch "Python Challenge"
#
# Copyright 2020 by Michael Inden


from turtle import Turtle, Screen


def hilbert_curve(n, turtle, angle=90):
    if n <= 0:
        return

    turtle.left(angle)
    hilbert_curve(n - 1, turtle, -angle)
    turtle.forward(1)
    turtle.right(angle)
    hilbert_curve(n - 1, turtle, angle)
    turtle.forward(1)
    hilbert_curve(n - 1, turtle, angle)
    turtle.right(angle)
    turtle.forward(1)
    hilbert_curve(n - 1, turtle, -angle)
    turtle.left(angle)


depth = 6
size = 2 ** depth

screen = Screen()
screen.setworldcoordinates(0, 0, size, size)

turtle = Turtle('turtle')
turtle.speed('fastest')
turtle.penup()
turtle.goto(0.5, 0.5)
turtle.pendown()

hilbert_curve(depth, turtle)

turtle.hideturtle()

screen.exitonclick()
