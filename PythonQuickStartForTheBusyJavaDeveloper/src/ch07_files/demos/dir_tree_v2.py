import os
from os.path import expanduser


def print_directory(current_dir, path, level):

    os.chdir(current_dir)
    files = os.listdir()

    for i, file in enumerate(files):
        is_last = i == len(files) - 1

        print("    " * level, end="")
        if is_last:
            print("\-- ", end="")
        else:
            print("|-- ", end="")

        print(file)

        if os.path.isdir(file):
            print_directory(file, path + file, level + 1)

    # Wechsel zurück in das aktuelle Verzeichnis
    if path != "":
        os.chdir("..")


os.chdir("..")
print_directory(os.getcwd(), "", 0)
