class EveryNth:
    def __init__(self, values, step, pos=0):
        # TODO
        pass

    def __iter__(self):
        return self

    def __next__(self):
        # TODO
        pass


thirdst_list = EveryNth([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 3)
print(list(thirdst_list))

thirdst_list = EveryNth([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 4, 2)
print(list(thirdst_list))

fifth_list = EveryNth([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 5)
print(list(fifth_list))
