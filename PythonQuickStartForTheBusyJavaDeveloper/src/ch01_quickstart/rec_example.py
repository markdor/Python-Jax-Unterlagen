def print_count_down_rec(value):
    # rekursiver Abbruch
    if value <= 0:
        print("FINISH")
        return

    print(value)
    # rekursiver Abstieg
    print_count_down_rec(value - 1)


print_count_down_rec(3)