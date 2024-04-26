from enum import Enum, auto


class Jahreszeiten(Enum):
    FRÜHLING = auto()
    SOMMER = auto()
    HERBST = auto()
    WINTER = auto()


class Size(Enum):
    XS = auto()
    S = auto()
    M = auto()
    L = auto()
    XL = auto()
    XXL = auto()


shirt_size = Size.XL
print(shirt_size)

for name in Jahreszeiten:
    print(name)
    print(name.value)