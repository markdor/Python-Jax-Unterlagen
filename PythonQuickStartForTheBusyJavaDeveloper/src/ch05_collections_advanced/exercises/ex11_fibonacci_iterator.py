class FibonacciIterator:
    def __init__(self, n=0):
        pass

    def __iter__(self):
        pass

    def __next__(self):
        pass


# create an Iterator
numbers = FibonacciIterator(10)
# create an iterable from the object
i = iter(numbers)
# Using next to get to the next iterator element
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))

for i in FibonacciIterator(10):
    print(i)