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


my_car = Car("VW", "ORANGE", 123)
print(my_car)

my_car.paint_with("GREEN")
my_car.apply_tuning_kit()
print(my_car)

my_car.paint_with("RED")
my_car.apply_tuning_kit()
print(my_car)