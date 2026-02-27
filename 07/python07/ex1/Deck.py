from ex0.Card import Card
from ex1.SpellCard import SpellCard
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard


class Deck():
    def __init__(self):
        self.lst_deck = []

    def add_card(self, card: Card) -> None:
        if isinstance(card, Card):
            self.lst_deck.append(card)
        else:
            print("card not recognized")

    def remove_card(self, card_name: str) -> bool:
        for card in self.lst_deck:
            if card.name == card_name:
                self.lst_deck.remove(card)
                return True
            return False

    def shuffle(self) -> None:
        from random import shuffle
        shuffle(self.lst_deck)

    def draw_card(self) -> Card:
        if (len(self.lst_deck) >= 1):
            card = self.lst_deck[0]
            self.lst_deck.pop(0)
            return (card)

    def get_deck_stats(self) -> dict:
        return {"total_card": len(self.lst_deck),
                "creature": len([x for x in self.lst_deck
                                if isinstance(x, CreatureCard)]),
                "spell": len([x for x in self.lst_deck
                              if isinstance(x, SpellCard)]),
                "artifact": len([x for x in self.lst_deck
                                 if isinstance(x, ArtifactCard)])}
