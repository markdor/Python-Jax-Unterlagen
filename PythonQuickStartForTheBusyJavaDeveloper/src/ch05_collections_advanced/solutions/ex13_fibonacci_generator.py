def fib_gen():

    yield 1
    yield 1

    fib1 = 1
    fib2 = 1

    while True:
        fib = fib1 + fib2
        yield fib

        fib2 = fib1
        fib1 = fib


def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x + y
        yield x


def square(nums):
    for num in nums:
        yield num ** 2


values = list(fibonacci_numbers(10))
print("fib", values)

values = list(square(fibonacci_numbers(10)))
print("fib squared", values)
