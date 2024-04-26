import turtle


def draw_one():
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)


def spacing():
    turtle.penup()
    turtle.forward(50)
    turtle.pendown()


def draw_two():
    turtle.forward(75)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(75)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(75)


# von unten nach oben
def draw_three():
    turtle.forward(75)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(75)
    turtle.back(75)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(75)


draw_one()
spacing()
draw_two()
spacing()
draw_three()

turtle.hideturtle()
turtle.exitonclick()

