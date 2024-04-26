def min_of_3(x, y, z):
    if x < y:
        if x < z:
            return x
        else:
            return z
    else:
        if y < z:
            return y
        else:
            return z


# print("SURPRISE", min_of_3(7, 2, 1))

def min_of_3(x, y, z):
    return min(x, min(y, z))


# print(min_of_3(7, 2, 1))


def main():
    print(min_of_3(7, 2, 1))
    print(min_of_3(7, 2, 1))


if __name__ == "__main__":
    main()