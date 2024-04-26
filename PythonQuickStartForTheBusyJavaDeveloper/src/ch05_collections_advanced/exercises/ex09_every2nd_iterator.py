class Every2nd:
    # TODO

    def __iter__(self):
        pass

    def __next__(self):
        pass


second_list = Every2nd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(list(second_list))
