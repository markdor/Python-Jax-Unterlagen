languages = ["Java", "Python"]
versions = [20.0, 3.11]

print(list(zip(languages, versions)))


number_list = [1, 2, 3]
str_list = ['one', 'two', 'three']

# Two iterables are passed
result = list(zip(number_list, str_list))
print(result)


# Converting iterator to set
result_set = set(result)
print(result_set)


number_list = [1, 2, 3, 4, 5, 6]
str_list = ['one', 'two', 'three']

print(list(zip(number_list, str_list)))

# Two iterables are passed
# Strict => True => Traceback
result = list(zip(number_list, str_list, strict=True))
print(result)

