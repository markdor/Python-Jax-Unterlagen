def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        # TDOO
        pass

    return [0]


def square(nums):
    for num in nums:
        yield num ** 2


for fib in fibonacci_numbers(10):
    print("fib", fib)
