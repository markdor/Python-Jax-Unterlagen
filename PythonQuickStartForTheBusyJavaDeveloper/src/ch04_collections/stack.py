class Stack:
    def __init__(self):
        self._values = []

    def push(self, elem):
        self._values.append(elem)

    def pop(self):
        if self.is_empty():
            raise StackIsEmptyException()
        return self._values.pop()

    def peek(self):
        if self.is_empty():
            raise StackIsEmptyException()
        return self._values[-1]

    def is_empty(self):
        return len(self._values) == 0


class StackIsEmptyException(Exception):
    pass
