# @dataclass

class SimplePerson:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return  f"SimplePerson {self.name} is {self.age} years old"

    def __repr__(self):
        return f"{self.name}  {self.age}"

    # by name
    def __lt__byname(self, other):
        return self.name < other.name

    # by name and age
    def __lt__(self, other):
        if self.name == other.name:
            return self.age < other.age
        return self.name < other.name

    def __eq__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.name, self.age) == (other.name, other.age)


peter30 = SimplePerson("Peter", 30)
peter65 = SimplePerson("Peter", 65)
michael51 = SimplePerson("Michael", 51)
michael21 = SimplePerson("Michael", 21)
michael51b = SimplePerson("Michael", 51)


persons = [peter65, michael51, peter30, michael21, michael51b]

# TypeError: '<' not supported between instances of 'SimplePerson' and 'SimplePerson'
persons.sort()

# benötigt __lt__()
persons.sort()
print(persons)

# benötigt __eq__
print(michael51 == michael51b)


#####################################################

from dataclasses import dataclass

@dataclass
class Position:
    name: str
    lon: float
    lat: float


pos = Position('Zürich', 17.15, 21.01)
print(pos)
print(f'{pos.name} is at {pos.lat}°N, {pos.lon}°E')


@dataclass
class SimPerson:
    name: str
    age: int

    # by name
    def __lt__(self, other):
        return self.name < other.name


michael1 = SimPerson("Micha", 42)
print(michael1)

michael2 = SimPerson("Micha", 42)
print(michael2)

michael3 = SimPerson("Michael", 51)
print(michael3)

print(michael1 == michael2)

michas = [michael1, michael3, michael2]
print(michas)
# TypeError: '<' not supported between instances of 'SimPerson' and 'SimPerson'
michas.sort()
print(michas)