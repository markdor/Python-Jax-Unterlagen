import math


class Rect:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return f"{self.x}, {self.y} - {self.width},  {self.height}"

    def draw(self):
        print("Drawing ... " + str(self))

    def area(self):
        print("Area ... " + str(self.width * self.height))


class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def __str__(self):
        return f"{self.x}, {self.y} x {self.radius}"

    def draw(self):
        print("Drawing ... " + str(self))

    def area(self):
        print("Area ... " + str(math.pi * self.radius ** 2))


class AmbigiousMultiFigure(Circle, Rect):
    def __init__(self, x, y, value):
        # V1
        #self.x = x
        #self.y = y
        #self.width = value
        #self.height = value
        #self.radius = value

        # V2 für (Rect, Circle):
        #super().__init__(x, y, value, value)
        #self.radius = value

        # V3 für (Circle, Rect):
        super().__init__(x, y, value)
        self.width = value
        self.height = value

    def area(self):
        print("Area 1... " + str(self.width * self.height))
        print("Area 2... " + str(math.pi * self.radius ** 2))


def main():
    r1 = Rect(0, 0, 10, 20)
    c1 = Circle(21, 42, 100)
    amf = AmbigiousMultiFigure(21, 42, 100)

    for shape in [r1, c1, amf]:
        shape.draw()
        shape.area()


if __name__ == "__main__":
    main()
