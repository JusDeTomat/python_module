from functools import reduce, partial, lru_cache, singledispatch
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    ops: dict[str, callable] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }
    selected_function = ops[operation]
    return reduce(selected_function, spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
        'Sharpness': partial(base_enchantment, 'Sharpness', 5),
        'Protection': partial(base_enchantment, 'Protection', 5),
        'Unbreaking': partial(base_enchantment, 'Unbreaking', 3)
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        return 0
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    @singledispatch
    def cast_spell(arg: any) -> str:
        raise TypeError("Type non supporté")

    cast_spell.register(int, lambda x: f'dealing {x} damage')
    cast_spell.register(str, lambda x: f'enchanting {x}')
    cast_spell.register(list, lambda x: f'casting barrage on: {x}')

    return cast_spell


def main():
    print("Testing spell reducer")
    spells = [10, 5, 2]
    print(f'Addition: {spell_reducer(spells, "add")}')
    print(f'Multiplication: {spell_reducer(spells, "multiply")}')

    print("\nTesting partial_enchanter")

    def enchanted(type_e: str, power: int, item: str) -> str:
        return f"{item} enchanted whit {type_e} {power}"
    enchant = partial_enchanter(enchanted)
    print(enchant['Sharpness']('sword'))
    print(enchant['Unbreaking']('shield'))

    print("\nTesting memoized fibinacci")
    print(memoized_fibonacci(200))
    print(memoized_fibonacci(40))
    memoized_fibonacci.cache_clear()

    print("\nTesting spell dispatcher")
    sd = spell_dispatcher()
    print(sd(8))
    print(sd([9, 9, 3, 32, 34]))
    print(sd("helmet"))


if (__name__ == "__main__"):
    main()
