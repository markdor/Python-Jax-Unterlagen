names = ["Mike", "Andy", "Peter", "Jim", "Tim"]

# alphabetisch (gemäss __lt__())
names.sort()
print(names)

# alphabetuisch absteugend
names.sort(reverse=True)
print(names)

# by 2nd char
names.sort(key=lambda name: name[2])
print(names)

# by last char
names.sort(key=lambda name: name[-1])
print(names)

# nach Länge
names.sort(key=len)
print(names)

# nach Länge absteigend
names.sort(key=len, reverse=True)
print(names)
