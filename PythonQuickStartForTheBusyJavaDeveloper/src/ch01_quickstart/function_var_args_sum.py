def var_args_sum(info, *args):
    result = 0
    for num in args:
        result += num
    return info + str(result)


print(var_args_sum("Summe: ", 1,2,3,4,5,6,7))
