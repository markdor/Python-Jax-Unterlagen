class SuperHero:
    def __init__(self, name, superpower, strength):
        self.name = name
        self.superpower = superpower
        self.__strength = strength

    def __str__(self):
        return f"{self.name} has {self.superpower} of strengths {self.__strength}"

    def is_stronger_than(self, other):
        return self.__strength > other.__strength

    def strongest_of(*heros):
        strongest_hero = None
        for hero in heros:
            if strongest_hero is None or hero.is_stronger_than(strongest_hero):
                strongest_hero = hero
        return strongest_hero

    def strongest_of_v2(*heros):
        if len(heros) == 0:
            return None

        strongest_hero = heros[0]
        for hero in heros[1:]:
            if hero.is_stronger_than(strongest_hero):
                strongest_hero = hero
        return strongest_hero

    def getstrength(self):
        return self.__strength


def main():
    superman = SuperHero("Superman", "Kryptonite-Power", 1_000)
    batman = SuperHero("Batman", "Techno-Power", 100)
    ironman = SuperHero("Ironman", "Techno-Power", 500)
    hulk = SuperHero("Hulk", "Angryness-Power", 10_000)

    print("Superman stronger than Batman?",
          superman.is_stronger_than(batman))
    print(SuperHero.strongest_of(superman, batman, ironman))
    print(SuperHero.strongest_of_v2(superman, batman, ironman, hulk))

    def extract_strength(hero):
        return hero.getstrength()

    print("Strongest", max([superman, batman, ironman, hulk], key=lambda hero: hero.getstrength()))
    print("Strongest", max([superman, batman, ironman, hulk], key=extract_strength))



if __name__ == "__main__":
    main()