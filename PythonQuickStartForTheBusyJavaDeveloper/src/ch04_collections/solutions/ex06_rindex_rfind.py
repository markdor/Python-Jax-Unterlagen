def last_index_of(values, search_for):
    for pos in range(len(values) - 1, -1, -1):
        if values[pos] == search_for:
            return pos

    return -1


def rfind(values, search_for):
    pos = last_index_of(values, search_for)
    if pos != -1:
        return pos

    raise ValueError(str(search_for) + " not found")


print(last_index_of([1, 2, 3, 2, 4, 2, 5, 2], 2))  # => 7
print(last_index_of([1, 2, 3, 2, 4, 2, 5, 2], 7))  # => -1
#print(rfind([1, 2, 3, 2, 4, 2, 5, 2], 7))  # => 7


######################################

def last_index_of(values, search_for, startpos = None):
    if not startpos:
        startpos = len(values) - 1
    for pos in range(startpos, -1, -1):
        if values[pos] == search_for:
            return pos

    return -1


def rfind(values, search_for, startpos = None):
    pos = last_index_of(values, search_for, startpos)
    if pos != -1:
        return pos

    raise ValueError(str(search_for) + " not found")


print(last_index_of([1, 2, 3, 2, 4, 2, 5, 2], 2, 6))  # => 5
print(last_index_of([1, 2, 3, 2, 4, 2, 5, 2], 2, 4))  # => 3
