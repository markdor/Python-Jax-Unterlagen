import os

os.chdir(".")
files = os.listdir()

for current in files:
    size = os.path.getsize(current)
    is_dir = os.path.isdir(current)

    dir_marker = "[DIR]" if is_dir else " "
    size_info_marker = " -/- " if is_dir else " " + str(size)

    print(current + size_info_marker + dir_marker)
