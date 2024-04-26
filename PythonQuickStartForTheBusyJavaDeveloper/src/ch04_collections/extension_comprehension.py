endings = ["st", "nd", "rd"] + 17 * ["th"] + \
          ["st", "nd", "rd"] + 7 * ["th"] + \
          ["st"]

for i in range(1, 32):
    print(str(i) + endings[i - 1])
