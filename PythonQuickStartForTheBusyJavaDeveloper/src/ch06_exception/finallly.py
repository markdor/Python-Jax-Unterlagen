names = ["Tim", "Tom", "Mike"]
try:
    print("INVALID INDEX: " + names[42])
except:
    print("wrong index")
finally:
    print("ALWAYS EXECUTED")