file = open("test.txt", encoding='utf-8')
try:
    # Datei lesen und verarbeiten
    pass
finally:
    file.close()

with open("test.txt", encoding='utf-8') as file:
    # Datei lesen und verarbeiten
    pass
