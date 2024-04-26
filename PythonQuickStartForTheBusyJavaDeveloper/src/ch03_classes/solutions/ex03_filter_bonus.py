from abc import ABC, abstractmethod


class AbstractFilter(ABC):
    @abstractmethod
    def filter(self, values):
        pass


class ExcludeFilter(AbstractFilter):
    def __init__(self, blocked=[]):
        self.__blocked = blocked

    def filter(self, values):
        return [x for x in values if x not in self.__blocked]


class IncludeFilter(AbstractFilter):
    def __init__(self, included=[]):
        self.__included = included

    def filter(self, values):
        return [x for x in values if x in self.__included]


class SPAMFilter(ExcludeFilter):
    def __init__(self):
        super().__init__(["SPAM"])


class NameFilter(IncludeFilter):
    def __init__(self):
        super().__init__(["MICHAEL", "SOPHIE"])


def main():
    basefilter = SPAMFilter()
    print(basefilter.filter(["SPAM", "DAS", "IST", "SPAM", "SPAM", "DETECTED"]))

    basefilter = NameFilter()
    print(basefilter.filter(["DAS", "SIND", "MICHAEL", "UND", "SOPHIE"]))


if __name__ == "__main__":
    main()
