def flexi_print(*values):
    print(*values)
    print(values)


flexi_print("ONE")
flexi_print("ONE", "TWO")
flexi_print("ONE", "TWO", "THREE")

