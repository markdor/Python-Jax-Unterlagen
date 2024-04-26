def even_generator():
    result = 0
    while True:
        yield result
        result += 2


def odd_generator():
    result = 1
    while True:
        yield result
        result += 2


for i in even_generator():
    print(i)
    if i > 10:
        break


for i in odd_generator():
    print(i)
    if i > 10:
        break


