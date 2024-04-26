cities = ["Kiel", "Hamburg", "Zürich", "Bremen",
          "Hamburg", "Zürich", "Kiel", "Bremen"]

cities_set = set(cities)
print(cities_set)

numbers1 = {1, 1, 2, 3, 5, 8, 13, 21}
numbers2 = {1, 2, 3, 4, 5, 6, 7}

print(numbers1 | numbers2)
print(numbers1 & numbers2)
print(numbers1 - numbers2)
print(numbers2 - numbers1)
print(numbers1 ^ numbers2)  # Vereinigung von
print((numbers1 - numbers2) | (numbers2 - numbers1))
