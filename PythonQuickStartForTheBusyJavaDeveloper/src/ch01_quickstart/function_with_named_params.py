def parameter_example(first, second):
    print("first:", first)
    print("second:", second)


parameter_example(1, 22)
parameter_example(second = 22, first = 1)


def parameter_example_4(first, second, third, forth):
    print("first:", first)
    print("second:", second)
    print("third:", third)
    print("forth:", forth)


parameter_example_4(1, 2, forth=44, third=33)
# Positional argument after keyword argument
#parameter_example_4(forth=44, 1, 2, third=33)