
# Named Tuple vs Class
from collections import namedtuple

Person = namedtuple('Person', ['name', 'age'])

persons = [Person("Mike", 50), Person("Tim", 50),
           Person("Tom", 7), Person("Jim", 30)]

# filter
older_than_30 = list(filter(lambda person: person.age > 30, persons))
print(older_than_30)

# map
half_aged = list(map(lambda person: person.age // 2, persons))
print(half_aged)

########################
# LIST COMPREHENSIONS
########################

older_than_30 = [person for person in persons if person.age > 30]
print(older_than_30)

half_aged = [person.age // 2 for person in persons]
print(half_aged)