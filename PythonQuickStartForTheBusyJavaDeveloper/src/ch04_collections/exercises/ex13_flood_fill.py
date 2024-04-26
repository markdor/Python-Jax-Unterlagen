def flood_fill(values2dim, x, y):
    pass


def print2dnice(values):
    for line in values:
        print("".join(line))


first_world = [list("   #  "),
               list("    # "),
               list("#   # "),
               list(" # #  "),
               list("  #   ")]
print2dnice(first_world)
flood_fill(first_world, 2, 2, "$")
print2dnice(first_world)

second_world = [list("   #      # "),
                list("    #      #"),
                list("#   #     # "),
                list(" # #     #  "),
                list("  #     #   ")]
print2dnice(second_world)
flood_fill(second_world, 5, 0, "$")
print2dnice(second_world)