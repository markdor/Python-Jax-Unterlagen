def contains_sequence(seq, values):
    pass


values = [0, "ABC", 42.195, True, 1, 2, 3]

print(contains_sequence(["ABC"], values))
print(contains_sequence([0, 1, 2, 3], values))
print(contains_sequence(["ABC", True, 2, 3], values))
print(contains_sequence(["ABC", 42.195], values))

# False
print(contains_sequence([7, "ABC", 2, 3], values))
print(contains_sequence([False, "ABC", 2, 3], values))
print(contains_sequence([42.195, "ABC"], values))