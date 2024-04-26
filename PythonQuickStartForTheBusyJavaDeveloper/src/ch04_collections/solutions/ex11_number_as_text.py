def number_as_text(n):
    value = ""
    remaining_value = n
    while remaining_value > 0:
        remainder_as_text = digit_as_text(remaining_value % 10)
        remaining_value = remaining_value // 10
        value = remainder_as_text + " " + value
    return value.strip()


value_to_text_mapping = {
    0: "ZERO", 1: "ONE", 2: "TWO", 3: "THREE", 4: "FOUR",
    5: "FIVE", 6: "SIX", 7: "SEVEN", 8: "EIGHT", 9: "NINE"}


def digit_as_text(n):
    return value_to_text_mapping[n % 10]


# Variante
def digit_as_text(n):
    digits = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']
    return digits[n % 10]


def number_as_text(n):
    return ' '.join([digit_as_text(int(digit)) for digit in str(n)])


print(number_as_text(721971))
