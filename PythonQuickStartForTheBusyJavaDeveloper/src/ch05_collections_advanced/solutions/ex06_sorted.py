from operator import attrgetter, itemgetter

inhabitants_and_cities = [(15_000_000, "New York"), (400_000, "Zürich"),
                          (250_000, "Kiel"), (550_000, "Bremen"),
                          (2_000_000, "Hamburg"), (250_000, "Aachen")]

inhabitants_and_cities = sorted(inhabitants_and_cities, key=lambda x: x[0])
print(inhabitants_and_cities)

inhabitants_and_cities = sorted(inhabitants_and_cities, key=lambda x: x[1], reverse=True)
print(inhabitants_and_cities)

# Sortierung nach letztem Buchstaben der Stadt
inhabitants_and_cities = sorted(inhabitants_and_cities, key=lambda x: x[1][-1], reverse=True)
print(inhabitants_and_cities)

# Bonus: Wie sortiere ich bei Gleichheit nach mehreren Kriterien?! => Tupel angeben
inhabitants_and_cities = sorted(inhabitants_and_cities, key=lambda x: (x[0], x[1]))
print(inhabitants_and_cities)