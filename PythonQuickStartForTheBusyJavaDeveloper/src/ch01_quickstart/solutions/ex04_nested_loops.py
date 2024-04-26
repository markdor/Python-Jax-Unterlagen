def print_number_triangle(number_of_rows):
    for y in range(1, number_of_rows + 1):
        for x in range(1, y + 1):
            print(x, end="")
        print()


print_number_triangle(3)
print_number_triangle(4)


def print_triangle(number_of_rows):
    num = 1
    for y in range(1, number_of_rows + 1):
        for x in range(1, y + 1):
            print(num, end=" ")
            num += 1
        print()


print_triangle(4)