import alchemy


def methode_1():
    import alchemy.elements as e
    print("\nMethod 1 - Full module import:\n"
          f"alchemy.elements.create_fire(): {e.create_fire()}")


def methode_2():
    from alchemy.elements import create_water
    print("\nMethod 2 - Specific function import:\n"
          f"create_water(): {create_water()}")


def methode_3():
    from alchemy.potions import healing_potion as heal
    print("\nMethod 3 - Aliased import:\n"
          f"heal(): {heal()}")


def methode_4():
    from alchemy.elements import create_fire, create_earth
    print("\nMethod 4 - Multiple imports:\n"
          f"create_earth(): {create_earth()}\n"
          f"create_fire(): {create_fire()}\n"
          f"strength_potion(): {alchemy.potions.strength_potion()}")


def main():
    print("=== Import Transmutation Mastery ===")
    methode_1()
    methode_2()
    methode_3()
    methode_4()
    print("\nAll import transmutation methods mastered!")


if (__name__ == "__main__"):
    main()
