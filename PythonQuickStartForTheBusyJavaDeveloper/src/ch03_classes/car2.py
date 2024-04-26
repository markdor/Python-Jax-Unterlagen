class Car:
    def __init__(self):
        self.brand = None
        self.color = None
        self.horse_power = 0

    def __init__(self, brand, color, horse_power):
        self.brand = brand
        self.color = color
        self.horse_power = horse_power


#car = Car()
#print(car)

my_car = Car("VW", "YELLOW", 75)
print(my_car)