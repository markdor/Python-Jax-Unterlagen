try:
    value = int("7271")
    print("after parsing 1. result", value)

    value = int("ERROR")
    print("after parsing 2. result", value)

except ValueError:
    print("can't parse to integer")
