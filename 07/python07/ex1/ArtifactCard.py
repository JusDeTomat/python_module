from ..ex0.Card import Card

class Artifact(Card):
	def __init__(self, name: str, cost: int, rarity: str, durability: int, effect: str):
		super().__init__(name, cost, rarity)
		self.durability = durability
		self.effect = effect
		self.type = "Artifact"

	def play(self, game_state: dict) -> dict:
		print(f"Drew: {self.name} ({self.type})")
		return {'card_played': self.name, 'mana_used': self.cost, 
		        'effect': self.effect}
		
	def activate_ability(self) -> dict:
		return {'activate': True}