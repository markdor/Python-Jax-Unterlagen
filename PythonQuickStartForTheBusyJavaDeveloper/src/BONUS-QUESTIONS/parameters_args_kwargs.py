# Variable Argumente
#     *args (Non Keyword Arguments)
#     **kwargs (Keyword Arguments)

def multiply(*num):
    result = 1

    for n in num:
        result = result * n

    print("multiply:", result)


multiply(3, 5)
multiply(7, 2, 7)
multiply(1, 2, 3, 4, 5)


##################################################

def variable_keyword_dict_like_args(**data):
    print("\nData type of argument:", type(data))
    print(data)

    for key, value in data.items():
        print("{} is {}".format(key, value))


variable_keyword_dict_like_args(Firstname="James", Lastname="Last", Age=22, Phone=1234567890)
variable_keyword_dict_like_args(Firstname="Holly", Lastname="Wood", Email="hollywood@nomail.com", Country="USA", Age=34,
                                Phone=9876543210)
