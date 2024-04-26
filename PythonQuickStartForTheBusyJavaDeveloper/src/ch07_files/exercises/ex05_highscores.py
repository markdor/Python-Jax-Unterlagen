from collections import namedtuple

# TODO

def read_highscores_from_csv(file_name):
    highscores = []

    # TODO

    return highscores


def extract_highscore_from(line):
    # TODO
    pass


def is_empty_line_or_comment(values):
    # TODO
    pass


def main():
    highscores_from_csv = read_highscores_from_csv("Highscores.csv")
    print("Highscores:")
    for highscore in highscores_from_csv:
        print(highscore)


if __name__ == "__main__":
    main()
