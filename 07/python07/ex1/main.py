from .Deck import Deck
from .SpellCard import SpellCard
from .ArtifactCard import Artifact
from ..ex0.CreatureCard import CreatureCard

def main():
	print("=== DataDeck Deck Builder ===\n\n"
		  "Drawing and playing cards:")
	deck = Deck()
	lst_card = [SpellCard("Lightning Bolt", 3, "Common", "damage"),
                Artifact("Mana Crystal", 2, "Common", 5, "Permanent: +1 mana per turn"),
				CreatureCard("Fire Dragon", 5, "'Legendary", 7, 5)]
	for card in lst_card:
		deck.add_card(card)
	deck.shuffle()
	for _ in range(3):
		card = deck.draw_card()
		print()
		play_result = card.play({})
		print(f"Play result: {play_result}")



if (__name__ == "__main__"):
	main()