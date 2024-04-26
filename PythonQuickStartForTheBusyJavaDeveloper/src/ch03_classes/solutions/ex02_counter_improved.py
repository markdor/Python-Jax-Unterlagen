class Counter:
    def __init__(self):
        self.__value = 0

    def current_value(self):
        return self.__value

    def increment(self):
        self.__value += 1

    def increment_by(self, value):
        self.__value += value

    def reset(self):
        self.__value = 0


def main():
    # Counter erzeugen, 2x hochzählen und dann resetten
    cnt = Counter()
    cnt.increment()
    cnt.increment()
    print(cnt.current_value())
    cnt.reset()
    cnt.increment_by(10)
    print(cnt.current_value())


if __name__ == "__main__":
    main()


