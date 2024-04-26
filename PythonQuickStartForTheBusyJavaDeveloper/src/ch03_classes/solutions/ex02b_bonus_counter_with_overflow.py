from ch03_classes.solutions.ex02_counter_improved import Counter


class CounterWithOverflow(Counter):
    COUNTER_MAX = 100

    def __init__(self):
        super().__init__()
        self.__overflow_count = 0

    def increment(self):
        super().increment()
        if self.current_value() >= self.COUNTER_MAX:
            super().reset()
            self.__overflow_count += 1

    def reset(self):
        super().reset()
        self.__overflow_count = 0

    def overflow_count(self):
        return self.__overflow_count


def main():
    points = CounterWithOverflow()

    for i in range(2021):
        points.increment()

    print("Points:", points.current_value())
    print("Bonus-Lifes:", points.overflow_count())


if __name__ == "__main__":
    main()