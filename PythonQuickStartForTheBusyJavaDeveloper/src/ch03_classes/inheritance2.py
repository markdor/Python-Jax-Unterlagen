class Base:
    def do_it(self):
        pass

    def do_that(self):
        pass


class Sub(Base):
    def do_it(self):
        print("do_it in Sub")


class SubSub(Sub):
    def do_that(self):
        print("do_that in SubSub")


print(issubclass(Sub, Base))
print(issubclass(SubSub, Base))
print(issubclass(SubSub, Sub))
