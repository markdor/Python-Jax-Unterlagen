import os
from os.path import expanduser


def print_directory(current_dir, path, level):

    os.chdir(current_dir)
    files = os.listdir()

    for file in files:
        print("    " * level, end="")
        print(file)

        if os.path.isdir(file):
            print_directory(file, path + file, level + 1)

    # Wechsel zurück in das aktuelle Verzeichnis
    if path != "":
        os.chdir("..")


os.chdir("..")
print_directory(os.getcwd(), "", 0)

