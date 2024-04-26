def rindex(values, item):
    reversed_values = values[::-1]
    return len(values) - reversed_values.index(item) - 1


last_index = lambda values, item: len(values) - values[::-1].index(item) - 1


values = ['Start', 'End', 'Mid', 'End']
print(values.index("End"))
print(rindex(values, "End"))
print(last_index(values, "End"))
print(rindex(values, "Start"))

