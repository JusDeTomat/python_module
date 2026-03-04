def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combined(args: any) -> tuple[any, any]:
        return (spell1(args), spell2(args))
    return combined


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def power(nb: int) -> int:
        return sum([base_spell(nb) * multiplier])
    return power


def conditional_caster(condition: callable, spell: callable) -> callable:
    def caster(mana: int, target: str) -> str:
        if condition(mana):
            return spell(target)
        return "Spell fizzled"
    return caster


def spell_sequence(spells: list[callable]) -> callable:
    def sequence(target: str) -> list[str]:
        return [spell(target) for spell in spells]
    return sequence


def main() -> None:
    def fireball(target: str) -> str:
        return f"Fireball hits {target}"

    def heal(target: str) -> str:
        return f"Heals {target}"

    def amplifier(nb: int) -> int:
        return nb

    def cond(nb: int) -> int:
        return nb > 10

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    print(combined("Dragon"))

    print("\nTesting power amplifier...")
    power_amp = power_amplifier(amplifier, 3)
    print(power_amp(10))

    print("\nTesting conditionnal caster")
    cc = conditional_caster(cond, fireball)
    print(cc(3, 'Dragon'))
    print(cc(30, 'Dragon'))

    print("\nTesting spell sequence")
    ss = spell_sequence([fireball, heal])
    print(ss('Dragon'))


if (__name__ == "__main__"):
    main()
