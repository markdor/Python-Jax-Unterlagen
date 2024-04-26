class SPAMFilter:
    def __init__(self, blocked="SPAM"):
        self.__blocked = blocked

    def filter(self, values):
        return [x for x in values if x not in self.__blocked]


class NameFilter:
    def __init__(self, included=[]):
        self.__included = included

    def filter(self, values):
        return [x for x in values if x in self.__included]


def main():
    basefilter = SPAMFilter()
    print(basefilter.filter(["SPAM", "DAS", "IST", "SPAM", "SPAM", "DETECTED"]))

    basefilter = NameFilter(["MICHAEL", "SOPHIE"])
    print(basefilter.filter(["DAS", "SIND", "MICHAEL", "UND", "SOPHIE"]))


if __name__ == "__main__":
    main()
