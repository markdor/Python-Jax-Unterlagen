from enum import Enum, auto
from collections import namedtuple

dxdy = namedtuple('dxdy', ['dx', 'dy'])

class Direction(Enum):
    N = dxdy(0, -1)
    NE = dxdy(1, -1)
    E = dxdy(1, 0)
    SE = dxdy(1, 1)
    S = dxdy(0, 1)
    SW = dxdy(-1, 1)
    W = dxdy(-1, 0)
    NW = dxdy(-1, -1)
