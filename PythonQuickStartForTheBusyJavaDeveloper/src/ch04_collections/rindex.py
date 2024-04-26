def rindex(values, item):
    reversed_values = values[::-1]
    return len(values) - reversed_values.index(item) - 1


values = ['Start', 'End', 'Mid', 'End']
print(values.index("End"))
print(rindex(values, "End"))
print(rindex(values, "Start"))

