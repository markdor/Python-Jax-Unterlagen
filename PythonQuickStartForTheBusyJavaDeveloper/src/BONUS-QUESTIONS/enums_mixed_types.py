from enum import Enum, auto


class Special(Enum):
     INT = 47
     STRING = "SPECIAL"
     TUPLE = (1, -1)


print(Special.INT.value)
print(Special.TUPLE.value)


def type_checker(sp):
     match (sp):
          case Special.INT:
               print("I am an INTEGER")
          case Special.STRING:
               print("I am a STRING")
          case Special.TUPLE:
               print("I am a TUPLE")


print(type_checker(Special.INT))
