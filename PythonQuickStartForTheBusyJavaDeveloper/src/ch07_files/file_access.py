file = open("test.txt", encoding = 'utf-8')
# perform file operations
file.close()


file = open("test.txt", encoding='utf-8')
try:
    # perform file operations
    pass
finally:
    file.close()


with open("test.txt", encoding = 'utf-8') as file:
    # perform file operations
    pass