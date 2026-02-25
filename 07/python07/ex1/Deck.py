from ..ex0.Card import Card
from .SpellCard import SpellCard
from .ArtifactCard import Artifact
from ..ex0.CreatureCard import CreatureCard
from random import shuffle

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
					lst_card.remove(card)
					return True
			return False

	def shuffle(self) -> None:
		shuffle(self.lst_deck)

	def draw_card(self) -> Card:
		if (len(self.lst_deck) >= 1):
			card = self.lst_deck[0]
			self.lst_deck.pop(0)
			return (card)
		

	def get_deck_stats(self) -> dict:
		return {"total_card": (len(self.lst_artifact) + len(self.lst_creature) + len(self.lst_spell)),
		"creature": len(self.lst_creature),
		"spell": len(self.lst_spell),
		"artifact": len(self.lst_artifact)}