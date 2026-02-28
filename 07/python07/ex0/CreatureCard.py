from typing import Any, Dict

from ex0.Card import Card


class CreatureCard(Card):
    """Concrete implementation of a creature card.

    Creature cards have attack and health stats and can be played to
    summon a creature onto the battlefield.
    """

    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 health: int) -> None:
        """Create a creature card.

        Args:
            name: Card name.
            cost: Mana cost.
            rarity: Rarity string.
            attack: Attack value.
            health: Health points.
        """
        self.name = name
        self.cost = cost
        self.rarity = rarity
        self.attack = attack
        self.health = health
        self.type = "Creature"

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        """Play this creature card.

        Args:
            game_state: Mapping representing the current game state.

        Returns:
            A dictionary describing the play action and mana used.
        """
        print(f"Drew: {self.name} ({self.type})")
        print(f"Playing {self.name} with {game_state.get('mana', 0)}"
              "mana available:\n"
              f"Playable: {self.is_playable(game_state.get('mana', 0))}")
        return {"card_played": self.name, 'mana_used': self.cost,
                "effect": 'Creature summoned to battlefield'}

    def get_card_info(self) -> Dict[str, Any]:
        """Return a dictionary with this card's metadata and stats."""
        return {"name": self.name, "cost": self.cost, "rarity": self.rarity,
                "type": self.type, "attack": self.attack,
                "health": self.health}

    def attack_target(self, target: Dict[str, Any]) -> Dict[str, Any]:
        """Attack a target described by a mapping.

        Args:
            target: Mapping with keys like 'name' and 'hp'.

        Returns:
            A dictionary describing the combat result.
        """
        print(f"{self.name} attacks {target.get('name', 'enemy')}:")
        return {'attacker': self.name, 'target': target.get('name', 'enemy'),
                'damage_dealt': self.attack,
                'combat_resolved': (target.get('hp', 0) - self.attack <= 0)}
