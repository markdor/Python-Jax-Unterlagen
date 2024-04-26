class Counter:
    def __init__(self):
        self.__count = 0

    def get_counter(self):
        return self.__count

    def set_counter(self, count):
        self.__count = count

    def reset(self):
        self.__count = 0


def main():
    # Counter erzeugen, 2x hochzählen und dann resetten
    cnt = Counter()
    cnt.set_counter(cnt.get_counter() + 1)
    cnt.set_counter(cnt.get_counter() + 1)
    print(cnt.get_counter())
    cnt.reset()
    print(cnt.get_counter())


if __name__ == "__main__":
    main()

