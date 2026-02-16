def test_ingredient():
    import alchemy.grimoire.validator as val
    print("Testing ingredient validation:")
    print("validate_ingredients('fire air'): "
          f"{val.validate_ingredients("fire air")}")
    print("validate_ingredients('dragon scales')"
          f"{val.validate_ingredients('dragon scales')}")


def test_spell():
    import alchemy.grimoire.spellbook as sell
    print("Testing spell recording with validation:")
    print("record_spell('Fireball', 'fire air'): "
          f"{sell.record_spell("Fireball", "fire air")}")
    print("record_spell('Dark Magic', 'shadow'):"
          f"{sell.record_spell("Dark Magic", "shadow")}")


def test_late():
    from alchemy.grimoire.spellbook import record_spell
    print("Testing late import technique:")
    print("record_spell('Lightning', 'air'):"
          f"{record_spell("Lightning", "air")}")


if (__name__ == "__main__"):
    print("=== Circular Curse Breaking ===\n")
    test_ingredient()
    print()
    test_spell()
    print()
    test_late()
    print("\nCircular dependency curse avoided using late imports!\n"
          "All spells processed safely!")
