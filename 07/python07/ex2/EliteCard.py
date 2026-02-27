class EliteCard(Card, Combatable, Magical):
	def __init__(self,name: str,cost: int,
        rarity: str,damage: int,health: int,combat_type: str,):
		pass
		
	
	def cast_spell(self, spell_name: str, targets: list) -> dict:
		pass

	def channel_mana(self, amount: int) -> dict:
		pass

	def get_magic_stats(self) -> dict:
		pass
