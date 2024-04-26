import random


def fac_generator(n=0):
    iteration = 1
    result = 1
    while iteration <= n:
        yield result
        iteration += 1
        result *= iteration


numbers = fac_generator(5)
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))

for i in fac_generator(5):
    print(i)


#############################

text = "X"

def square(nums):
    for num in nums:
        print(num)
        print(len(text))
        yield num ** len(text)


for i in square(fac_generator(5)):
    print(i)
    text += "X" * random.randint(1, 5)
    print(text)