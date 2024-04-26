class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def adjust_to_dir(self, direction):
        return Position(self.x + direction.value.dx,
                        self.y + direction.value.dy)
