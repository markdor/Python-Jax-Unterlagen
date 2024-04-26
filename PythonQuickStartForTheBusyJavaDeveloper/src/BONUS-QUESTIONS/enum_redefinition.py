from enum import Enum, auto


class Size(Enum):
    XS = auto(); S = auto(); M = auto()
    L = auto()
    #XL = "XL"
    XL = 42
    XXL = auto()
    #XXL = "XXL"


shirt_size = Size.XL
print(shirt_size)

print(Size.XS.value, Size.S.value, Size.M.value, Size.L.value, Size.XL.value)

# redefinition => AttributeError: Cannot reassign members.
#Size.XXL = 47
print(Size.XXL)
print(Size.XXL.value)
