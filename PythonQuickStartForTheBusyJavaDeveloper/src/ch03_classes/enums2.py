from collections import namedtuple
from enum import Enum


class Direction(Enum):
     N = (0, -1)
     NE = (1, -1)
     E = (1, 0)
     SE = (1, 1)
     S = (0, 1)
     SW = (-1, 1)
     W = (-1, 0)
     NW = (-1, -1)


print(Direction.NE.value)
ne = Direction.NE
print(ne.value[0], "/", ne.value[1])


############ ADD ON

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


print(Direction.NE.value)
ne = Direction.NE
print(ne.value.dx, "/", ne.value.dy)
