# Beispielprogramm für das Buch "Python Challenge"
#
# Copyright 2020 by Michael Inden


from turtle import Turtle, Screen


def sierpinski_points(turtle, depth, mid_x, mid_y, boxsize):
    if depth < 0:
        return

    turtle.up()
    # ohne das wird alles durcheinander, wenn die Figur nicht korrekt geschlossen wurde (genug Drehunhgen)
    turtle.setheading(0)
    turtle.goto(mid_x - boxsize // 2, mid_y + boxsize // 2)

    # draw filled rect
    turtle.down()
    turtle.begin_fill()
    turtle.forward(boxsize)
    turtle.right(90)
    turtle.forward(boxsize)
    turtle.right(90)
    turtle.forward(boxsize)
    turtle.right(90)
    turtle.forward(boxsize)
    turtle.end_fill()

    if depth > 0:
        # for all direction
        dir_offsets = [(-1, -1), (0, -1), (1, -1),
                       (-1, 0), (1, 0),
                       (-1, 1), (0, 1), (1, 1)]

        for offset in dir_offsets:
            new_boxsize = boxsize // 3
            new_x = mid_x + offset[0] * boxsize
            new_y = mid_y + offset[1] * boxsize
            sierpinski_points(turtle, depth - 1, new_x, new_y, new_boxsize)

depth = 3
screen = Screen()
screen.setworldcoordinates(0, 0, 400, 400)

turtle = Turtle()
turtle.speed('fastest')
turtle.penup()

sierpinski_points(turtle, depth, 200, 200, 100)

turtle.hideturtle()

screen.exitonclick()
