from ex1.Deck import Deck
from ex1.SpellCard import SpellCard
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard


def main() -> None:
    """Demonstrate adding cards to a deck and playing a card."""
    print("=== DataDeck Deck Builder ===\n\n"
          "Drawing and playing cards:")
    deck = Deck()
    lst_card = [SpellCard("Lightning Bolt", 3, "Common", "damage"),
                ArtifactCard("Mana Crystal", 2, "Common", 5,
                             "Permanent: +1 mana per turn"),
                CreatureCard("Fire Dragon", 5, "'Legendary", 7, 5)]
    for card in lst_card:
        deck.add_card(card)
    print(f"Deck stats: {deck.get_deck_stats()}")
    deck.shuffle()
    for _ in range(3):
        card = deck.draw_card()
    print()
    play_result = card.play({})
    print(f"Play result: {play_result}")
    print("\nPolymorphism in action: Same interface, "
          "different card behaviors!")


if (__name__ == "__main__"):
    main()
