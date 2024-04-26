import math
from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Rect(Figure):
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


class Circle(Figure):
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


def main():
    r1 = Rect(0, 0, 10, 20)
    c1 = Circle(21, 42, 100)
    r2 = Rect(20, 2, 120, 220)
    c2 = Circle(221, 42, 100)

    for shape in [r1, c1, r2, c2]:
        shape.draw()
        shape.area()


if __name__ == "__main__":
    main()


