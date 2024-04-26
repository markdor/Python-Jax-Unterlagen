class FactorialIterator:
    def __init__(self, n=0):
        self.n = n
        self.result = 1
        self.iteration = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.iteration > self.n:
            raise StopIteration
        self.result *= self.iteration
        self.iteration += 1
        return self.result


# create an Iterator
numbers = FactorialIterator(5)
# create an iterable from the object
i = iter(numbers)
# Using next to get to the next iterator element
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
# print(next(i))

for i in FactorialIterator(5):
    print(i)
