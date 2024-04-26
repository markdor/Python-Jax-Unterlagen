from abc import ABC


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


class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def __str__(self):
        return f"{self.x}, {self.y} x {self.radius}"

    def draw(self):
        print("Drawing ... " + str(self))


def main():
    r1 = Rect(0, 0, 10, 20)
    c1 = Circle(21, 42, 100)
    r2 = Rect(20, 2, 120, 220)
    c2 = Circle(221, 42, 100)

    for shape in [r1, c1, r2, c2]:
        shape.draw()


if __name__ == "__main__":
    main()


