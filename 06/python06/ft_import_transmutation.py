def method_1() -> None:
    import alchemy.elements as e
    print("\nMethod 1 - Full module import:\n"
          f"alchemy.elements.create_fire(): {e.create_fire()}")


def method_2() -> None:
    from alchemy.elements import create_water
    print("\nMethod 2 - Specific function import:\n"
          f"create_water(): {create_water()}")


def method_3() -> None:
    from alchemy.potions import healing_potion as heal
    print("\nMethod 3 - Aliased import:\n"
          f"heal(): {heal()}")


def method_4() -> None:
    from alchemy.elements import create_fire, create_earth
    from alchemy.potions import strength_potion
    print("\nMethod 4 - Multiple imports:\n"
          f"create_earth(): {create_earth()}\n"
          f"create_fire(): {create_fire()}\n"
          f"strength_potion(): {strength_potion()}")


def main() -> None:
    print("=== Import Transmutation Mastery ===")
    method_1()
    method_2()
    method_3()
    method_4()
    print("\nAll import transmutation methods mastered!")


if (__name__ == "__main__"):
    main()
