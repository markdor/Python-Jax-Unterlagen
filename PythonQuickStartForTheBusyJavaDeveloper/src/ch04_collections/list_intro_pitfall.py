cities = ["Zürich", "Luzern"]
cities += ["Bremen", "Aachen"]

print(cities)

cities.extend(["Paris", "London"])
print(cities)

# Fallstrick
cities.extend("OSLO")
cities += "KIEL"
print(cities)