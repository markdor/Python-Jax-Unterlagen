def matches_pattern(pattern, input):
    # Vorbereitung
    values = input.split(" ")
    if len(values) != len(pattern) or (len(values) == 1 and not values[0]):
        return False

    placeholder_to_value_map = {}

    # Durchlaufe alle Zeichen
    for i, pattern_char in enumerate(pattern):
        value = values[i]
        # füge hinzu, sofern noch nicht da
        if not pattern_char in placeholder_to_value_map:
            placeholder_to_value_map[pattern_char] = value
        # stimmt gespeicherter Wert mit aktueller Zeichenfolge überein?
        assigned_value = placeholder_to_value_map[(pattern_char)]
        if not assigned_value == value:
            return False
    return True


print(matches_pattern("xyyx", "tim mike mike tim"))
print(matches_pattern("xyyx", "tim mike tom tim"))
