def func1():
    func2()


def func2():
    func3()


def func3():
    raise ValueError


def main():
    func1()


if __name__ == "__main__":
    main()
