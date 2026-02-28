from typing import List, Optional, Dict

from ex0.Card import Card
from ex1.SpellCard import SpellCard
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard


class Deck:
    """Simple list-backed deck container for cards."""

    def __init__(self) -> None:
        """Initialize an empty deck."""
        self.lst_deck: List[Card] = []

    def add_card(self, card: Card) -> None:
        """Add a card to the deck.

        Args:
            card: Instance of :class:`Card` (or subclass).
        """
        if isinstance(card, Card):
            self.lst_deck.append(card)
        else:
            print("card not recognized")

    def remove_card(self, card_name: str) -> bool:
        """Remove the first card matching `card_name`.

        Args:
            card_name: Name of the card to remove.

        Returns:
            True if a card was removed, False otherwise.
        """
        for card in self.lst_deck:
            if card.name == card_name:
                self.lst_deck.remove(card)
                return True
            return False

    def shuffle(self) -> None:
        """Shuffle the deck in-place."""
        from random import shuffle

        shuffle(self.lst_deck)

    def draw_card(self) -> Optional[Card]:
        """Draw the top card from the deck.

        Returns:
            The drawn :class:`Card` instance or None if the deck is empty.
        """
        if len(self.lst_deck) >= 1:
            card = self.lst_deck[0]
            self.lst_deck.pop(0)
            return card
        return None

    def get_deck_stats(self) -> Dict[str, int]:
        """Return simple counts about the deck composition."""
        return {
            "total_card": len(self.lst_deck),
            "creature": len([
                x for x in self.lst_deck
                if isinstance(x, CreatureCard)
            ]),
            "spell": len([
                x for x in self.lst_deck
                if isinstance(x, SpellCard)
            ]),
            "artifact": len([
                x for x in self.lst_deck
                if isinstance(x, ArtifactCard)
            ]),
        }
