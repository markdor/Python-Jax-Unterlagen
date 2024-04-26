from abc import ABC, abstractmethod

class Base(ABC):
   # @abstractmethod
    def do_it(self):
        pass

    # @abstractmethod
    def do_that(self):
        pass


class Sub(Base):
    def do_it(self):
        print("do_it in Sub")


class SubSub(Sub):
    def do_that(self):
        print("do_that in SubSub")


obj = Base()

obj = Sub()
#obj.do_that()