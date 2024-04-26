# Beispielprogramm für das Buch "Einfach Python"
#
# (C) 2021 Michael Inden

from collections import namedtuple

Person = namedtuple('Person', 'name age')

persons = [Person("Mike", 37), Person("Tim", 49),
           Person("Tom", 5), Person("Michael", 50),
           Person("Jim", 7), Person("James", 17)]

adults = [person for person in persons if person.age >= 18]
print(adults)

adult_names = [person.name for person in persons if person.age >= 18]
print(adult_names)
print("---".join(adult_names))

adult_sum_of_ages = sum([person.age for person in persons if person.age >= 18])
print(adult_sum_of_ages)

# List comprehension flachgeklopft
result = []
for person in persons:
    if person.age >= 18:
        result += [person]