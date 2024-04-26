numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(numbers[2:8])

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(numbers[0:3])

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(numbers[-3:])

#####################################

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(numbers[0::2])
print(numbers[2:10:2])
print(numbers[10:2:-2])

#####################################

numbers = [0, 1, 2, 3, 9, 10, 11, 12]
print(numbers)
numbers[4:4] = [4, 5, 6, 7, 8]
print(numbers)
numbers[4:8] = [44, 55, 66, 77, 88]
print(numbers)
numbers[0:14:2] = ["X", "X", "X", "X", "X", "X", "X"]
print(numbers)
numbers[0:14:2] = ["XXX"] * 7
print(numbers)
numbers[1:-1] = []
print(numbers)