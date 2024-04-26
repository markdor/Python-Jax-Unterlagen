def check_braces(input):
    opening_count = 0
    for ch in input:
        if ch == "(":
            opening_count += 1
        elif ch == ")":
            opening_count -= 1
            if opening_count < 0:
                return False

    return opening_count == 0


print(check_braces("(())"))
print(check_braces("())"))