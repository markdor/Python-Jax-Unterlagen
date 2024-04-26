add_one = lambda x: x + 1
double_it = lambda x: x * 2
mult = lambda a, b : a * b
power_of = lambda x, y: x ** y

print(double_it(7))
print(power_of(2,8))


sample_numbers = [1, 5, 4, 6, 8, 11, 3, 12]
is_even = lambda x: (x % 2 == 0)
only_even_numbers = list(filter(is_even, sample_numbers))
print(only_even_numbers)


sample_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
doubled_numbers = list(map(lambda x: x * 2, sample_numbers))
print(doubled_numbers)

squared_numbers = list(map(lambda x: x * x, sample_numbers))
print(squared_numbers)


continents = ["Afrika", "Asia", "South America", "North America",
              "Europe", "Australia", "Antarctica"]
result = map(len, continents)
print(list(result))