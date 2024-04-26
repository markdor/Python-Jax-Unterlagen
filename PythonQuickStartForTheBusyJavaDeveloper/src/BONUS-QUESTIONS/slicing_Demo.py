values = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Index Assigment
values[4] = [4444, 5555, 6666, 7777]
print(values)

# Insert
values[2:2] = [22, 222, 2222, 22222]
print(values)

# Remove
values[2:6] = []
print(values)

# ACHTUNG
values[2:6] = [9, 9, 9, 9, 9, 9, 9, 9]
print(values)

# Schrittweite + ungültige Exception
values[2:12:2] = [1, 2, 3, 4, 5, 6, 7]
print(values)