def remove_duplicates(inputs):
    result = []
    already_found_numbers = set()

    for elem in inputs:
        if elem not in already_found_numbers:
            already_found_numbers.add(elem)
            result.append(elem)
    return result


print(remove_duplicates([7, 2, 7, 1]))
print(remove_duplicates([1, 6, 6, 6, 1, 2]))


def remove_duplicates(inputs):
    result = []
    for i in inputs:
        if i not in result:
            result += [i]
    return result


def remove_duplicates(inputs):
    result = []
    [result.append(i) for i in inputs if i not in result]
    return result


print(remove_duplicates([7, 2, 7, 1]))
print(remove_duplicates([1, 6, 6, 6, 1, 2]))
