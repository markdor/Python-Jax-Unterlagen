
names = ["Tim", "Tom", "Mike"]
names += ["Jim", "Peter"]
print(names)

doubles = [value * 2 for value in range(10) if value % 2 != 0]
squares = [value * value for value in range(10) if value % 2 == 0]
odds = [value * 2 for value in range(10) if value % 2 != 0]
evens = [value ** 2 for value in range(10) if value % 2 == 0]
print(doubles)
print(squares)
print(odds)
print(evens)


def even_double_odd_next_even(n):
    if n % 2 == 0:
        return n * 2
    else:
        return n + 1


result = [even_double_odd_next_even(value) for value in range(10)]
print(result)


def even_triple_odd_next_even(n):
    if n % 2 == 0:
        return n * 3
    else:
        return n + 1


result = [even_triple_odd_next_even(value) for value in range(10)]
print(result)


def special(n):
    if n % 2 == 0:
        return n * 2 + 1
    else:
        return n * 2 - 1


result = [special(value) for value in range(10)]
print(result)


multi_dim = [[x, y * 2] for x in range(3) for y in range(5)]
print(multi_dim)