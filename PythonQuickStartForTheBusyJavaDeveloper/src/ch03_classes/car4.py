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


my_car = Car("VW", "YELLOW", 75)
print(my_car)

print(my_car.brand)

my_car.color = "STEALTH_BLACK"
my_car.horse_power += 250
print(my_car)

