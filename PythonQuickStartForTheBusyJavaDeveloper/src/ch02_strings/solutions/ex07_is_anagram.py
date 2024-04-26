def is_anagram(str1, str2):
    char_counts1 = calc_char_frequencies(str1)
    char_counts2 = calc_char_frequencies(str2)

    return char_counts1 == char_counts2


def calc_char_frequencies(input):
    char_counts = {}
    for current_char in input.upper():
        if current_char in char_counts:
            char_counts[current_char] += 1
        else:
            char_counts[current_char] = 1
    return char_counts


print(is_anagram("Ampel", "Lampe"))
print(is_anagram("Ampel", "Palme"))
print(is_anagram("Palme", "Lampe"))
print(is_anagram("Palme", "Alpen"))


###############################
# coole Variante
def is_anagram_v2(str1, str2):
    str1_as_list = sorted(list(str1.lower()))
    str2_as_list = sorted(list(str2.lower()))

    return str1_as_list == str2_as_list


print(is_anagram_v2("Ampel", "Lampe"))
print(is_anagram_v2("Ampel", "Palme"))
print(is_anagram_v2("Palme", "Lampe"))
print(is_anagram_v2("Palme", "Alpen"))
