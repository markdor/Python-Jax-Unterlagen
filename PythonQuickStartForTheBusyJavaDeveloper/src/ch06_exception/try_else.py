try:
    num = int(input("Enter a number between 0 - 99: "))
    assert 0 <= num < 100
except AssertionError:
    print("Not a valid number between 0 - 99!")
else:
    reciprocal = 1/num
    print(reciprocal)