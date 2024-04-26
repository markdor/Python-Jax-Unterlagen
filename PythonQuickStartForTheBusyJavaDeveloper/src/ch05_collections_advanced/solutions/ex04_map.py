# Achtung Fallstrick, weil String Iterable ist
countries = ["USA", "Schweiz", "Deutschland", "Frankreich", "Italien"]
result = list(map(reversed, countries))
print(result)

# Zwischenschritt
result = list(map(reversed, countries))
for i in result:
    print("".join(i))

result = list(map("".join, map(reversed, countries)))
print(result)

result = list(map(lambda x: x[::-1], countries))
print(result)
