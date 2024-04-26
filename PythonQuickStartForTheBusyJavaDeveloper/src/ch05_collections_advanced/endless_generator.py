def endless_generator():
    result = 1
    while True:
        yield result
        result += 1


numbers = endless_generator()
print(next(numbers))
print(next(numbers))

for i in endless_generator():
    print(i)
    if i > 1_000:
        break