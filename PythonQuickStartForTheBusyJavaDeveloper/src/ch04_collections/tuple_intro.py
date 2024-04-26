cities_inhabitants = {"Kiel": 250_000,
                      "Bremen": 550_000,
                      "Zürich": 400_000}

city, inhabitant_count = cities_inhabitants.popitem()
print(city, inhabitant_count)

for key, value in cities_inhabitants.items():
    print(key, value)

first, second, *rest = (1, 2, 3, 4, "END")
print(first, second, rest)
