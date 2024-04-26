values = [[5, 1, 2],
          [1, 3, 5],
          [2, 5, 1],
          [3, 2, 3],
          [4, 4, 4]]


by_first_elem = sorted(values, key=lambda x: x[0])
print(by_first_elem)

by_second_elem = sorted(values, key=lambda x: x[1])
print(by_second_elem)

by_third_elem = sorted(values, key=lambda x: x[2])
print(by_third_elem)