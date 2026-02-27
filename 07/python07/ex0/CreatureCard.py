from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 health: int):
        self.name = name
        self.cost = cost
        self.rarity = rarity
        self.attack = attack
        self.health = health
        self.type = "Creature"

    def play(self, game_state: dict) -> dict:
        print(f"Drew: {self.name} ({self.type})")
        print(f"Playing {self.name} with {game_state.get('mana', 0)}"
              "mana available:\n"
              f"Playable: {self.is_playable(game_state.get('mana', 0))}")
        return {"card_played": self.name, 'mana_used': self.cost,
                "effect": 'Creature summoned to battlefield'}

    def get_card_info(self):
        return {"name": self.name, "cost": self.cost, "rarity": self.rarity,
                "type": self.type, "attack": self.attack,
                "health": self.attack}

    def attack_target(self, target: dict) -> dict:
        print(f"{self.name} attacks {target.get('name', 'enemy')}:")
        return {'attacker': self.name, 'target': target.get('name', 'enemy'),
                'damage_dealt': self.attack,
                'combat_resolved': (target.get('hp', 0) - self.attack <= 0)}
