from collections import namedtuple

Highscore = namedtuple('Highscore', 'name points level')


def read_highscores_from_csv(file_name):
    highscores = []

    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                highscore = extract_highscore_from(line)
                if highscore:
                    highscores.append(highscore)
    except IOError:
        print("processing of file '", file_name, "' failed!")

    return highscores


def extract_highscore_from(line):
    values = line.split(",")
    # Behandlung von Leerzeilen, Kommentaren und unvollständigen Einträgen
    if is_empty_line_or_comment(values) or len(values) != 3:
        return None

    try:
        # Auslesen der Werte als String + Typprüfung
        name = values[0].strip()
        points = int(values[1].strip())
        level = int(values[2].strip())

        return Highscore(name, points, level)
    except ValueError:
        print("Skipping invalid point or level value '", values, "'")
        return None


def is_empty_line_or_comment(values):
    return ((len(values) == 1 and len(values[0].strip()) == 0) or
            # Ignoriere Kommentare, die auch ',' oder ';' enthalten
            (len(values) >= 1 and values[0].strip().startswith("#")))


def main():
    highscores_from_csv = read_highscores_from_csv("Highscores.csv")
    print("Highscores:")
    for highscore in highscores_from_csv:
        print(highscore)


if __name__ == "__main__":
    main()
