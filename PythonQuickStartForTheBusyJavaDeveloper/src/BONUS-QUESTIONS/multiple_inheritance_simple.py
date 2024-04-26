class Animal:
    def info(self):
        print("i am an animal")


class WingedAnimal:
    def winged_animal_info(self):
        print("yeah, hopefully I can fly")


class Bat(Animal, WingedAnimal):
    pass


bat = Bat()
bat.info()
bat.winged_animal_info()
