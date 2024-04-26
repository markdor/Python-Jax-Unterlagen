from functools import total_ordering, cmp_to_key

data = [("ABC", "DEF", 2), ("ABCD", "DEFG", 3),
        ("ZZZ", "ZEBRA", 0), ("ZZZ", "AAA", 5),
        ("CCC", "DDD", 1), ("CCC", "FFF", 4), ("CCC", "AAA", 6), ("CCC", "AAA", 7), ("CCC", "AAA", 5)]

data.sort(key=lambda x: (x[0], x[1]))
print(data)

data.sort(key=lambda x: (x[0], x[2]))
print(data)

data.sort(key=lambda x: (x[0], -x[2]))
print(data)

print("################################")
from operator import itemgetter, attrgetter

data = [("ABC", "DEF", 2), ("ABCD", "DEFG", 3),
        ("ZZZ", "ZEBRA", 0), ("ZZZ", "AAA", 5),
        ("CCC", "DDD", 1), ("CCC", "FFF", 4), ("CCC", "AAA", 6), ("CCC", "AAA", 7), ("CCC", "AAA", 5)]

# Trick, aber mehrere Sortiervorgänge: sort ist stabil, mit kleinstem Kriterium starten
data.sort(key=itemgetter(1), reverse=True)
data.sort(key=itemgetter(0))
print(data)
# Trick, aber mehrere Sortiervorgänge
data.sort(key=itemgetter(2), reverse=True)
data.sort(key=itemgetter(1), reverse=True)
data.sort(key=itemgetter(0))
print(data)
print("################################")


def multisort(values, specs):
    for key, order in reversed(specs):
        should_reverse = order == "desc" or order == "DESC"
        values.sort(key=itemgetter(key), reverse=should_reverse)
    return values



data = [("ABC", "DEF", 2), ("ABCD", "DEFG", 3),
        ("ZZZ", "ZEBRA", 0), ("ZZZ", "AAA", 5),
        ("CCC", "DDD", 1), ("CCC", "FFF", 4), ("CCC", "AAA", 6), ("CCC", "AAA", 7), ("CCC", "AAA", 5)]

ret = multisort(data, [(0, "asc"), (1, "desc")])
print(ret)

ret = multisort(data, [(0, "asc"), (1, "desc"), (2, "desc")])
print(ret)
print("################################")


def multisort_by_attr(values, specs):
    for key, order in reversed(specs):
        should_reverse = order == "desc" or order == "DESC"
        values.sort(key=attrgetter(key), reverse=should_reverse)
    return values

#ret = multisort_by_attr(data, [("name", "asc"), ("age", "desc"), ("city", "desc")])
#print(ret)