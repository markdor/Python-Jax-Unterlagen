def contains_sequence(seq, values):
    last_pos = 0
    for val in seq:
        # ACHTUNG: False und 0 werden gleich behandelt!!!
        # ACHTUNG: ValueError!!
        try:
            found = values.index(val)
            # Spezialbehandlung für Typcheck
            if type(val) is not type(values[found]):
                raise ValueError
        except ValueError:
            found = -1

        if found == -1:
            return False

        if found < last_pos:
            return False

        last_pos = found

    return True


values = [0, "ABC", 42.195, True, 1, 2, 3]

print(contains_sequence(["ABC"], values))
print(contains_sequence([0, 1, 2, 3], values))
print(contains_sequence(["ABC", True, 2, 3], values))
print(contains_sequence(["ABC", 42.195], values))

# False
print(contains_sequence([7, "ABC", 2, 3], values))
print(contains_sequence([False, "ABC", 2, 3], values))
print(contains_sequence([42.195, "ABC"], values))