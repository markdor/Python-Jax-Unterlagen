names = ["Tim", "Tom", "Mike"]
for i in range(5):
    try:
        value = int(names[i])
    except (ValueError, ZeroDivisionError):
        print("can't parse to integer")
    except IndexError:
        print("wrong index")


names = ["Tim", "Tom", "Mike"]
for i in range(5):
    try:
        value = int(names[i])
    except (ValueError, ZeroDivisionError) as ex:
        print("can't parse to integer:", ex)
    except IndexError as ie:
        print("wrong index:", ie)