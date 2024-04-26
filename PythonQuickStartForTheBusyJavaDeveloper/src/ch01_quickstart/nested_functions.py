def f():
    print("f1")

    def g():
        print("g!")

        # (noch) nicht sichtbar!
        # h()
        def h():
            print("h!")

        h()

    # nicht (mehr) sichtbar!
    # h()
    g()
    print("f2")

f()
print("nach f")