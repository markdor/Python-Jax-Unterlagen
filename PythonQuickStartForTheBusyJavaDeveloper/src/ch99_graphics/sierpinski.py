# Beispielprogramm für das Buch "Python Challenge"
#
# Copyright 2020 by Michael Inden


from turtle import Turtle, Screen


def calcMid(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)


def sierpinski(turtle, depth, points):
    if depth < 0:
        return

    turtle.up()
    # left corner
    turtle.goto(points[0][0], points[0][1])
    turtle.down()
    if depth == 0:
        turtle.begin_fill()
    turtle.goto(points[1][0], points[1][1])
    turtle.goto(points[2][0], points[2][1])
    turtle.goto(points[0][0], points[0][1])
    if depth == 0:
        turtle.end_fill()

    points1 = [points[0],
                calcMid(points[0], points[1]),
                calcMid(points[0], points[2])]
    points2 = [calcMid(points[0], points[1]),
               points[1],
               calcMid(points[1], points[2])]
    points3 = [calcMid(points[0], points[2]),
               calcMid(points[1], points[2]),
               points[2]]

    sierpinski(turtle, depth - 1, points1)
    sierpinski(turtle, depth - 1, points2)
    sierpinski(turtle, depth - 1, points3)



depth = 6
points = [[0,0], [150, 300], [300, 0]]

screen = Screen()
screen.setworldcoordinates(0, 0, 300, 300)

turtle = Turtle()
turtle.speed('fastest')
turtle.penup()
turtle.goto(0.5, 0.5)
turtle.pendown()

sierpinski(turtle, depth, points)

turtle.hideturtle()

screen.exitonclick()
