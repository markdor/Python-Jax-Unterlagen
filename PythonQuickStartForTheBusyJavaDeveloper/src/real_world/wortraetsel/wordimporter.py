def import_words():
    words = []
    file_name = "words.txt"
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                word = line.strip().upper()
                if is_relevant(word):
                    words.append(word)

    except IOError:
        print("processing of file '", file_name, "' failed!")

    return words


def is_relevant(word):
    return word and not is_comment(word)


def is_comment(word):
    return word.startswith("#") or word.startswith("//")

