from ex0.CreatureCard import CreatureCard


def main() -> None:
    """Small demo to exercise CreatureCard behavior."""
    dragon = CreatureCard("Fire Dragon", 5, "'Legendary", 7, 5)

    print(f"=== DataDeck Card Foundation ===\n"
          "Testing Abstract Base Class Design:\n"
          f"\nCreatureCard Info:\n{dragon.get_card_info()}\n")
    result = dragon.play({"mana": 200})
    print(f"Play result: {result}\n")

    result = dragon.attack_target({"name": " Goblin Warrior", "hp": 3})
    print(f"Attack result: {result}\n")

    nb_mana = 3
    print(f"Testing insufficient mana ({nb_mana} available):\n"
          f"Playable: {dragon.is_playable(nb_mana)}\n"
          "\nAbstract pattern successfully demonstrated!")


if (__name__ == "__main__"):
    main()
