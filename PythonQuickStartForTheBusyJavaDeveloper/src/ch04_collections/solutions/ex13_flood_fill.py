def flood_fill(values2dim, x, y):
    # $\mbox{\bfseries rekursiver Abbruch}$
    if x < 0 or y < 0 or x >= len(values2dim[0]) or y >= len(values2dim):
        return

    if values2dim[y][x] == ' ':
        values2dim[y][x] = '*'

        # $\mbox{\bfseries rekursiver Abstieg: fülle in alle 4 Richtungen}$
        flood_fill(values2dim, x, y - 1)
        flood_fill(values2dim, x + 1, y)
        flood_fill(values2dim, x, y + 1)
        flood_fill(values2dim, x - 1, y)


def print2dnice(values):
    for line in values:
        print("".join(line))


first_world = [list("   #  "),
               list("    # "),
               list("#   # "),
               list(" # #  "),
               list("  #   ")]
print2dnice(first_world)
flood_fill(first_world, 2, 2)
print2dnice(first_world)

second_world = [list("   #      # "),
                list("    #      #"),
                list("#   #     # "),
                list(" # #     #  "),
                list("  #     #   ")]
print2dnice(second_world)
flood_fill(second_world, 5, 0)
print2dnice(second_world)