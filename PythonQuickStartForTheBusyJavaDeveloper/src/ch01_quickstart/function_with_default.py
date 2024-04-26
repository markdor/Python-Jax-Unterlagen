def parameter_with_default(x, y, opt_info = "n/a"):
    print("(%d, %d)" % (x, y))
    print("Info:", opt_info)


parameter_with_default(7, 2)
parameter_with_default(72, 71, "OPT-VALUE")