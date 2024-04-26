def is_magic6(values):
    values_with_loop = list(values)
    # schließe das Dreieck
    values_with_loop.append(values[0])
    side1 = values_with_loop[0:3]
    side2 = values_with_loop[2:5]
    side3 = values_with_loop[4:7]

    return compare_sum_of_sides(side1, side2, side3)


def compare_sum_of_sides(side1, side2, side3):
    sum1 = sum(side1)
    sum2 = sum(side2)
    sum3 = sum(side3)
    return sum1 == sum2 and sum2 == sum3


print(is_magic6([1, 5, 3, 4, 2, 6]))
print(is_magic6([1, 2, 3, 4, 5, 6]))


def is_magic_triangle(values):
    if len(values) % 3 != 0:
        raise ValueError("Not a triangle: " + len(values))
    side_length = 1 + len(values) // 3
    values_with_loop = list(values)
    # schließe das Dreieck
    values_with_loop.append(values[0])
    side1 = values_with_loop[0: side_length]
    side2 = values_with_loop[side_length - 1: side_length * 2 - 1]
    side3 = values_with_loop[(side_length - 1) * 2: side_length * 3 - 2]

    return compare_sum_of_sides(side1, side2, side3)


def is_magic_triangle_v2(values):
    if len(values) % 3 != 0:
        raise ValueError("Not a triangle: " + len(values))
    side_length = 1 + len(values) // 3
    pos = 0
    sum_of_sides = [0, 0, 0]
    for current_side in range(3):
        for _ in range(side_length):
            sum_of_sides[current_side] += values[pos]
            # Trick 1: Mit Modulo => keine Spezialbehandlung für letzten Wert
            pos = (pos + 1) % len(values)

        # Trick 2: Die Seiten überlappen sich, Endfeld = nächstes Startfeld
        pos -= 1

    return sum_of_sides[0] == sum_of_sides[1] and \
           sum_of_sides[1] == sum_of_sides[2]


print(is_magic_triangle([1, 5, 3, 4, 2, 6]))
print(is_magic_triangle([1, 2, 3, 4, 5, 6]))

print(is_magic_triangle_v2([1, 5, 3, 4, 2, 6]))
print(is_magic_triangle_v2([1, 2, 3, 4, 5, 6]))