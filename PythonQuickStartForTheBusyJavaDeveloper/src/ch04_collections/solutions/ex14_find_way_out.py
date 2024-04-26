def find_way_out(values, x, y):
    if x < 0 or y < 0 or x > len(values[0]) or y >= len(values):
        return False

    # rekursiver Abbruch
    if values[y][x] == 'X':
        print("FOUND EXIT: x: {}, y: {}".format(x, y))
        return True

    # Mauer oder bereits besucht?
    if values[y][x] in '#.':
        return False

    # rekursiver Abstieg
    if values[y][x] == ' ':
        # markiere als besucht
        values[y][x] = '.'

        # versuche alle 4 Himmelsrichtungen
        up = find_way_out(values, x, y - 1)
        left = find_way_out(values, x + 1, y)
        down = find_way_out(values, x, y + 1)
        right = find_way_out(values, x - 1, y)

        found_a_way = up or left or down or right

        # Backtracking, weil keine gültige Lösung
        if not found_a_way:
            values[y][x] = ' '  # Feldmarkierung löschen

        return found_a_way

    raise ValueError("wrong char in labyrinth", values[y][x])


labyrinth = [list("##################################"),
             list("# #         #    #     #  #   X#X#"),
             list("#  ##### #### ##   ##  #  # ###  #"),
             list("#  ##  #    #  ## ##  #  #     # #"),
             list("#    #  ###  # ## ##   #   ### # #"),
             list("# #   ####     ## ##      ###  # #"),
             list("####   #     ####  ####  # ####  #"),
             list("######   #########   ##   # ###  #"),
             list("##     #  X X####X #  #  # ###  ##"),
             list("##################################")]

print(labyrinth)
find_way_out(labyrinth, 4, 1)

for line in labyrinth:
    print("".join(line))