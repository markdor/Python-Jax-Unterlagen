class EveryNth:
    def __init__(self, values, step):
        self.values = values
        self.pos = 0
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.pos >= len(self.values):
            raise StopIteration

        self.pos += self.step
        return self.values[self.pos - self.step]


thirdst_list = EveryNth([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 3)
print(list(thirdst_list))

fifth_list = EveryNth([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 5)
print(list(fifth_list))