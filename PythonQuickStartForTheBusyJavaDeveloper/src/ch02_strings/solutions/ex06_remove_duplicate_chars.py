def remove_duplicates(input):
    result = ""
    already_seen = set()
    for current_char in input:
        if not current_char in already_seen:
            already_seen.add(current_char)
            result += current_char
    return result


print(remove_duplicates("lalamlam"))
print(remove_duplicates("bananas"))
