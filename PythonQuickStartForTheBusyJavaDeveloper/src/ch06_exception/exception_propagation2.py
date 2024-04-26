from src.ch06_exception.custom_exception import ValueOutOfBoundsError


def func1(value):
    func2(value)


def func2(value):
    try:
        func3(value)
    except ValueOutOfBoundsError as voobe:
        print(voobe)


def func3(value):
    if not value:
        raise ValueError
    raise ValueOutOfBoundsError(value, 1, 100)


def main():
    func1(123)
    func1(None)


if __name__ == "__main__":
    main()
