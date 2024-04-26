import itertools

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(itertools.dropwhile(lambda x: x < 7, numbers)))

print(list(itertools.takewhile(lambda x: x < 7, numbers)))

print(list(itertools.takewhile(lambda x: x >=7,
           itertools.dropwhile(lambda x: x < 7, numbers))))