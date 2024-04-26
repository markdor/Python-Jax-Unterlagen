def find_way_out(values, x, y):
    pass


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