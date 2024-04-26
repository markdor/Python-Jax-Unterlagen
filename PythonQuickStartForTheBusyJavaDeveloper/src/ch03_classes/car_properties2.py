class Car:
    def __init__(self, brand, color, horse_power):
        self.__brand = brand
        self.__color = color
        self.horse_power = horse_power

    def __get_brand(self):
        print("__get_brand")
        return self.__brand

    def __get_color(self):
        print("__get_color")
        return self.__color

    def __get_horse_power(self):
        print("__get_horse_power")
        return self.__horse_power

    # additional
    def __set_horse_power(self, horse_power):
        if horse_power <= 0 or horse_power > 2_000:
            raise ValueError("INVALID PS: not in range 1 - 2000")
        self.__horse_power = horse_power

    def paint_with(self, color):
        print("paint_with")
        self.__color = color

    # property(fget, fset, fdel, doc)
    brand = property(__get_brand)
    color = property(__get_color, paint_with)
    horse_power = property(__get_horse_power, __set_horse_power)

    def __str__(self):
        return "{} {} with {} PS".format(self.color, self.brand, self.horse_power)


my_car = Car("RENAULT", "PETROL", 195)
#my_car.brand = "VW" # AttributeError: can't set attribute
my_car.color = "RED"
my_car.horse_power = 7271
print(my_car)