primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

result = list(filter(lambda x: 20 < x < 500, map(lambda x: x ** 3, primes)))
print(result)
