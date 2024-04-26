def remove_vowel(text):
    result = ""

    for letter in text:
        if letter not in "AÄEIOÖUüaäeioöuü":
            result += letter

    return result


# unelegant
def remove_vowel_ugly(text):
    result = text.replace("a", "").replace("ä", "").replace("e", "").replace("u", "").replace("ü", "").replace("o", "").replace("ö", "")

    return result


def remove_vowel_v2(text):
    vowels = [ "a", "ä", "e", "i", "o", "ö", "u", "ü"]
    vowels += [ "A", "Ä", "E", "I", "O", "Ö", "U", "ü"]

    for vowel in vowels:
        text = text.replace(vowel, "")

    return text


def is_vowel(letter):
    return letter in "AÄEIOÖUüaäeioöuü"


def remove_vowel_v3(text):
    return "".join([ch for ch in text if not is_vowel(ch)])


def replace_vowel(text, replacement="_"):
    result = ""

    for letter in text:
        if is_vowel(letter):
            result += replacement
        else:
            result += letter

    return result


def is_vowel(letter):
    return letter in "AÄEIOÖUüaäeioöuü"


print(remove_vowel("Es gibt viel zu entdecken!"))

print(replace_vowel("Es gibt viel zu entdecken!"))
print(replace_vowel("Es gibt viel zu entdecken!", "$$"))

text = "PYTHON INTRO BY MICHAEL"
print(replace_vowel(text))