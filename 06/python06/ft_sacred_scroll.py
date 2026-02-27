import alchemy.elements as ae
import alchemy as init


def main() -> None:
    print("=== Sacred Scroll Mastery ===\n")
    print("Testing direct module access:")
    print(f"alchemy.elements.create_fire(): {ae.create_fire()}\n"
          f"alchemy.elements.create_water(): {ae.create_water()}\n"
          f"alchemy.elements.create_earth(): {ae.create_earth()}\n"
          f"alchemy.elements.create_air(): {ae.create_air()}")
    print("\nTesting package-level access (controlled by __init__.py):")
    lst: list = []
    lst_fonc: list = ["create_fire", "create_water", "create_earth",
                      "create_air"]
    for element in lst_fonc:
        try:
            function = getattr(init, element)
            lst.append(function())
        except AttributeError:
            lst.append("AttributeError - not exposed")

    print(f"alchemy.create_fire(): {lst[0]}\n"
          f"alchemy.create_water(): {lst[1]}\n"
          f"alchemy.create_earth(): {lst[2]}\n"
          f"alchemy.create_air(): {lst[3]}")

    print("\nPackage metadata:\n"
          f"Version: {init.__version__}\n"
          f"Author: {init.__author__}")


if (__name__ == "__main__"):
    main()
