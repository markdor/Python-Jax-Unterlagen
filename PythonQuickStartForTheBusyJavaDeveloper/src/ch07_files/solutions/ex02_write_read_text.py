info = """This is the first line
This is the second line
Fun with multiline strings
This picture is brilliant
"""

with open("image-info.txt", 'w', encoding ='utf-8') as file:
    file.write(info)

with open("image-info.txt", 'r', encoding ='utf-8') as file:
    content = file.readlines()
    print(content)

with open("image-info.txt", 'a', encoding ='utf-8') as file:
    file.write("ADDITIONAL LINE-1\n")
    file.write("ADDITIONAL LINE-2\n")

with open("image-info.txt", 'r', encoding ='utf-8') as file:
    content = file.readlines()
    print(content)