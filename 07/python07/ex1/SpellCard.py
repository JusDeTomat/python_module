from ..ex0.Card import Card

class SpellCard(Card):
	def  __init__(self, name: str, cost: int, rarity: str, effect_type: str):
		super().__init__(name, cost, rarity)
		self.effect_type = effect_type
		self.type = "Spell"
	
	def play(self, game_state: dict) -> dict:
		print(f"Drew: {self.name} ({self.type})")
		return {'card_played': self.name, 'mana_used': self.cost, 
		        'effect': self.effect_type}

	def resolve_effect(self, targets: list) -> dict:
		return {
            'effect': self.effect_type,
            'targets': targets
        }