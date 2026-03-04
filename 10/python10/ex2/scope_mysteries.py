def mage_counter() -> callable:
    i = 0

    def count() -> int:
        nonlocal i
        i += 1
        return i
    return count


def spell_accumulator(initial_power: int) -> callable:
    power = initial_power

    def add_power() -> int:
        nonlocal power
        power += initial_power
        return power
    return add_power


def enchantment_factory(enchantment_type: str) -> callable:
    def enchant(item: str) -> str:
        return f"{item} enchanted whit {enchantment_type}"
    return enchant


def memory_vault() -> dict[str, callable]:
    security: dict[any, any] = {}

    def store(key: any, val: any) -> None:
        security[key] = val

    def recall(key: any) -> any:
        try:
            return security[key]
        except KeyError:
            return "Memory not found"

    return {"recall": recall, "store": store}


def main() -> None:
    print("Testing mage counter...")
    counter = mage_counter()
    print(f"Call 1: {counter()}")
    print(f"Call 2: {counter()}")
    print(f"Call 3: {counter()}")

    print("\nTesting spell accumulator")
    spell = spell_accumulator(5)
    print(f"Call 1: {spell()}")
    print(f"Call 2: {spell()}")
    print(f"Call 3: {spell()}")

    print("\nTesting enchantment_factory")
    enchated = enchantment_factory("Sharpness V")
    print(enchated("Diamond Sword"))

    print("\nTesting memory_vault")
    vault = memory_vault()
    vault['store']('name', 'Mathis')
    print(vault['recall']('name'))


if (__name__ == "__main__"):
    main()
