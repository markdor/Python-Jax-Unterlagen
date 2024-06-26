class Car:
    def __init__(self, brand, color, horse_power):
        self.brand = brand
        self.color = color
        self.horse_power = horse_power

    def __str__(self):
        return f"Marke: {self.brand} / Farbe: {self.color} /" + \
               f" PS: {self.horse_power}"

    def __repr__(self):
        return self.__str__()

    def paint_with(self, new_color):
        self.color = new_color

    def apply_tuning_kit(self):
        self.horse_power += 150

    def __eq__(self, other):
        if not isinstance(other, Car):
            return False

        return self.brand == other.brand and \
               self.color == other.color and \
               self.horse_power == other.horse_power


toms_car = Car("Audi", "BLUE", 275)
jims_car = Car("Audi", "BLUE", 275)

print(toms_car == jims_car) # Java "equals()"
print(toms_car is jims_car) # Java "=="
