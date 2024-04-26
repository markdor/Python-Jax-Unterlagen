with open("../personenliste.txt", 'w', encoding ='utf-8') as file:
    file.write("Person1: ch.open Michael\n")
    file.write("Person2: JAX Peter\n")
    file.write("This file contains three lines\n")


with open("../personenliste.txt", 'r', encoding ='utf-8') as file:
    content = file.read()
    print(content)


with open("../personenliste.txt", 'r', encoding ='utf-8') as file:
    # Zeilenweises Lesen
    for line in file:
        print(line, end='')


with open("../personenliste.txt", 'r', encoding ='utf-8') as file:
    lines = file.readlines()
    print("Lines", lines)


with open("../personenliste.txt", 'r', encoding ='utf-8') as file:
    count = 1
    line_content = file.readline()
    while line_content:
        print("Line", count, ": '", line_content, "'", end ="")
        line_content = file.readline()
        count += 1


with open("../personenliste.txt", encoding ='utf-8') as file:
    count = 1
    while line_content := file.readline():
        print("Line", count, ":", line_content, end ="")
        count += 1