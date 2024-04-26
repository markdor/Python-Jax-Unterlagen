def fac(n):
    if n == 0 or n == 1:
        return 1

    print("calling fac(" + str(n - 1) + ")")
    return n * fac(n - 1)


print(fac(5))


def fib(n):
    if n == 1 or n == 2:
        return 1

    return fib(n - 1) + fib(n - 2)


def fib_v2(n):
    if n == 0 or n == 1:
        return n

    return fib(n - 1) + fib(n - 2)


print(fib(5))
print(fib(6))
print(fib(8))
