values = (0, "ABC", 42.195, True)

print("ABC" in values)
print(["ABC", 42.195] in values)


def contains_sequence(seq, values):
    stringified_seq = "".join(str(i) for i in seq)
    stringified_values = "".join(str(i) for i in values)

    return stringified_seq in stringified_values


print(contains_sequence(["ABC"], values))
print(contains_sequence(["ABC", 42.195], values))



