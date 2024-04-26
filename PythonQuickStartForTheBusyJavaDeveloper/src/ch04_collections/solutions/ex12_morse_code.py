def to_morse_code(input):
    converted_msg = ""
    for current_char in input.upper():
        converted_letter = convert_to_morse_code(current_char)
        converted_msg += converted_letter
        converted_msg += "   "
    return converted_msg.strip()


def convert_to_morse_code(current_char):
    chars_to_morse = {"E": ".",
                      "O": "- - -",
                      "S": ". . .",
                      "T": "-",
                      "W": ". - -"}
    return chars_to_morse[current_char]
    #return chars_to_morse.get(current_char, "???")


print(to_morse_code("SOS"))
print(to_morse_code("TWEET"))
print(to_morse_code("OST"))