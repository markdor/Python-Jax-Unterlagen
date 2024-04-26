class FibonacciIterator:
    def __init__(self, n=0):
        self.n = n
        self.fib = 1
        self.fib1 = 1
        self.fib2 = 1
        self.iteration = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.iteration > self.n:
            raise StopIteration

        if self.iteration == 1 or self.iteration == 2:
            self.iteration += 1
            return 1

        self.fib = self.fib1 + self.fib2
        self.fib2 = self.fib1
        self.fib1 = self.fib
        self.iteration += 1
        return self.fib


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