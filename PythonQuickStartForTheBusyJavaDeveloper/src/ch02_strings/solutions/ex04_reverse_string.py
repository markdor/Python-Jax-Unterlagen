def reverse_string(input):
    # rekursiver Abbruch
    if len(input) <= 1:
        return input

    first_char = input[0]
    remaining = input[1:]

    # rekursiver Abstieg
    return reverse_string(remaining) + first_char


print(reverse_string("ABCDEFGHI"))
print(reverse_string("was it a car or a cat i saw"))

print("ABCDEFGHI"[::-1])