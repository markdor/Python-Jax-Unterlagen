def repeat_chars(input):
    result = ""

    for i, ch in enumerate(input):
        result += ch * (i + 1)

    return result


print(repeat_chars("ABCD"))
print(repeat_chars("ABCDEF"))


def repeat_chars_v2(input):
    return "".join([ch * (i + 1) for i, ch in enumerate(input)])

print(repeat_chars_v2("ABCD"))
print(repeat_chars_v2("ABCDEF"))