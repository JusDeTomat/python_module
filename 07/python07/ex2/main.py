
from ex2.EliteCard import EliteCard


def main():
    print("=== DataDeck Ability System ===\n\n"
          "EliteCard capabilities:\n"
          "- Card: ['play', 'get_card_info', 'is_playable']\n"
          "- Combatable: ['attack', 'defend', 'get_combat_stats']\n"
          "- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']\n")
    player = EliteCard('Arcane Warrior', 5, 'commun', 5, 10, 'melee')
    player.play({
        'ar': {'hp': 10},
        'dr': 5,
        'scs': 'Fireball',
        'sce': ['Enemy1', 'Enemy2'],
        'mc': 3
    })
    print("Multiple interface implementation successful!")


if (__name__ == "__main__"):
    main()
