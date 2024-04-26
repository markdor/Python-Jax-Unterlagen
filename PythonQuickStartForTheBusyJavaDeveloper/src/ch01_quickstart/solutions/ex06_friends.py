from src.ch01_quickstart.solutions.ex03_find_proper_divisors import find_proper_divisors


def calc_friends(max_exclusive):
    friends = {}
    for i in range(2, max_exclusive):
        divisors1 = find_proper_divisors(i)
        sum_div1 = sum(divisors1)
        divisors2 = find_proper_divisors(sum_div1)
        sum_div2 = sum(divisors2)

        if i == sum_div2 and sum_div1 != sum_div2:
            friends[i] = sum_div1
            print("i:", i)
            print("divisors1:", divisors1, "=>", sum_div1)
            print("divisors2:", divisors2, "=>", sum_div2)
            print()

    return friends


print("friends up to 2000", calc_friends(2000))