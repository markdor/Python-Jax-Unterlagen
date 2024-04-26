a = 11
b = 12
c = 77

if a > 10 and b < 20 and c > 50:
    print("a > 10 && b < 20 && c > 50")


def lt20(val):
    print("lt")
    return val < 20


def gt50(val):
    print("gt")
    return val > 50

print("============== SHORT CIRCUIT ============")
if a > 10 and lt20(b) and gt50(c):
    print("a > 10 && b < 20 && c > 50")

print("b=22")
b = 22
if a > 10 and lt20(b) and gt50(c):
    print("a > 10 && b < 20 && c > 50")

print("a=7")
a = 7
if a > 10 and lt20(b) and gt50(c):
    print("a > 10 && b < 20 && c > 50")
