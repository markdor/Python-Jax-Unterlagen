class SuperHero:
    def __init__(self, name, superpower, strength):
        # TODO
        pass

    def __str__(self):
        # TODO
        return ""

    def  is_stronger_than(self, other):
        # TODO
        return False

    def strongest_of(*heros):
        strongest_hero = None
        # TODO
        return strongest_hero


def main():
    superman = SuperHero("Superman", "Kryptonite-Power", 1_000)
    batman = SuperHero("Batman", "Techno-Power", 100)
    ironman = SuperHero("Ironman", "Techno-Power", 500)

    print("Superman stronger than Batman?",
          superman.is_stronger_than(batman))
    print(SuperHero.strongest_of(superman, batman, ironman))


if __name__ == "__main__":
    main()