class Car:
    def __init__(self, brand, color, horse_power):
        self.__brand = brand
        self.__color = color
        self.__horse_power = horse_power

    def __str__(self):
        return f"Marke: {self.__brand} / Farbe: {self.__color} /" + \
               f" PS: {self.__horse_power}"

    def __repr__(self):
        return self.__str__()

    def paint_with(self, new_color):
        self.__color = new_color

    def apply_tuning_kit(self):
        self.__horse_power += 150

    # Zugriff nach außen gewähren
    def brand(self):
        return self.__brand

    @property
    def horse_power(self):
        return self.__horse_power

    @horse_power.setter
    def horse_power(self, horse_power):
        if horse_power <= 0 or horse_power > 2_000:
            raise ValueError("INVALID PS: not in range 1 - 2000")

        self.__horse_power = horse_power

    def __eq__(self, other):
        if not isinstance(other, Car):
            return False
        return self.__brand == other.__brand and \
               self.__color == other.__color and \
               self.__horse_power == other.__horse_power


my_car = Car("Audi", "BLUE", 275)
my_car.horse_power = 1234
print(my_car.horse_power)