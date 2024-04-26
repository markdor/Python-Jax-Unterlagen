class EveryNthWithOffset:
    def __init__(self, values, step, offset=0):
        self.values = values
        self.pos = offset
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.pos >= len(self.values):
            raise StopIteration

        self.pos += self.step
        return self.values[self.pos - self.step]


values = EveryNthWithOffset([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2)
print(list(values))

values = EveryNthWithOffset(["TO", "BE", "SKIPPED", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4, 3)
print(list(values))