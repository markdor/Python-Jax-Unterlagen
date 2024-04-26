import os
from os.path import expanduser


def print_directory(current_dir, path, indent):

    os.chdir(current_dir)
    files = os.listdir()

    for i, file in enumerate(files):
        is_last = i == len(files) - 1

        print(indent, end="")
        if is_last:
            print("\-- ", end="")
        else:
            print("|-- ", end="")

        print(file)

        if os.path.isdir(file):
            new_indent = "    " if is_last else "|   "
            print_directory(file, path + file, indent + new_indent)

    # Wechsel zurück in das aktuelle Verzeichnis
    if path != "":
        os.chdir("..")


os.chdir("..")
print_directory(os.getcwd(), "", "")
