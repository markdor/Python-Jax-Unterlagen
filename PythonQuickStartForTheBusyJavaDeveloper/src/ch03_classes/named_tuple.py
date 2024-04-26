from collections import namedtuple


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y


origin = Point2D(0, 0)
print(origin)


Point2D = namedtuple('Point2D', ['x', 'y'])
Point2D = namedtuple('Point2D', ('x', 'y'))
Point2D = namedtuple('Point2D', 'x, y')
Point2D = namedtuple('Point2Db', "x y")
origin = Point2D(0, 0)
print(origin)
print(origin.x)
print(origin.y)

Person = namedtuple('Person', ['name', 'age'])

Top4 = namedtuple('Top4', ['first', 'second', 'third', "forth"])
pizza_top4 = Top4("Funghi", "Diavola", "Napoli", "Salami")

Top3 = namedtuple('Top3', ['first', 'second', 'third'])
pizza_top3 = Top3("Funghi", "Diavola", "Napoli")

print(pizza_top3)
print(pizza_top3[0], pizza_top3[1], pizza_top3[2])
print(pizza_top3.first, pizza_top3.second, pizza_top3.third)

# Tuple sind immutable
# pizza_top3[0] = "GYROS"