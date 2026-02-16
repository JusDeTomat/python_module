def absolute_import():
    from alchemy.transmuation.basic import lead_to_gold \
        as ltg, stone_to_gem as stg
    print("Testing Absolute Imports (from basic.py):\n"
          f"lead_to_gold(): {ltg()}\n"
          f"stone_to_gem(): {stg()}")


def relative_import():
    import alchemy.transmuation.advanced as path
    print("Testing Relative Imports (from advanced.py):\n"
          f"philosophers_stone(): {path.philosophers_stone()}\n"
          f"elixir_of_life(): {path.elixir_of_life()}")


def package_access():
    import alchemy.transmuation.__init__ as package
    print("Testing Package Access:"
          f"alchemy.transmutation.lead_to_gold(): {package.lead_to_gold()}\n"
          f"alchemy.transmutation.philosophers_stone(): "
          f"{package.philosophers_stone()}")


def main():
    print("=== Pathway Debate Mastery ===\n")
    absolute_import()
    print()
    relative_import()
    print()
    package_access()
    print()
    print("Both pathways work! Absolute: clear, Relative: concise")


if (__name__ == "__main__"):
    main()
