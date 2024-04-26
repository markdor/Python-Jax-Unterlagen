def my_second_generator():
    n=1
    print('This is printed first')
    yield n
    n += 2
    print('This is printed second')
    yield n
    n += 3
    print('This is printed at last')
    yield n


gen = my_second_generator()
# We can iterate through the items using next().
print(next(gen))
print(next(gen))
