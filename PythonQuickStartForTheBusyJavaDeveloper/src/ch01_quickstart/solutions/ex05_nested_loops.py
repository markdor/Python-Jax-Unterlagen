def print_letter_triangle(number_of_rows):
    letter = "A"
    for y in range(1, number_of_rows + 1):
        for x in range(1, y + 1):
            print(letter, end="")
        letter = chr(ord(letter) + 1)
        print()


print_letter_triangle(3)
print_letter_triangle(4)