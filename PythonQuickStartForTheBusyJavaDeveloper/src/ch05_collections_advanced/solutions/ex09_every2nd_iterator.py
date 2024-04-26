class Every2nd:
    def __init__(self, values):
        self.values = values
        self.pos = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.pos >= len(self.values):
            raise StopIteration

        self.pos += 2
        return self.values[self.pos - 2]


second_list = Every2nd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(list(second_list))
