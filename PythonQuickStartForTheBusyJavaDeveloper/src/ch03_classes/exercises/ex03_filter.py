class ExcludeFilter:
    def __init__(self, blocked = []):
        self.__blocked = blocked

    # TODO


class IncludeFilter:
    def __init__(self, included = []):
        self.__included = included

    # TODO


class SPAMFilter(ExcludeFilter):
    def __init__(self):
        # TODO
        pass


class NameFilter(IncludeFilter):
    def __init__(self):
        # TODO
        pass


def main():
    spamfilter = SPAMFilter()
    print(spamfilter.filter(["SPAM", "DAS", "IST", "SPAM", "SPAM", "DETECTED"]))

    namefilter = NameFilter()
    print(namefilter.filter(["DAS", "SIND", "MICHAEL", "UND", "SOPHIE"]))


if __name__ == "__main__":
    main()

