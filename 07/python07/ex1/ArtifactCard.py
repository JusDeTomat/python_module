from typing import Any, Dict

from ex0.Card import Card


class ArtifactCard(Card):
    """Concrete artifact card with durability and passive effect."""

    def __init__(self, name: str, cost: int, rarity: str, durability: int,
                 effect: str) -> None:
        """Initialize an artifact card.

        Args:
            name: Card name.
            cost: Mana cost.
            rarity: Rarity string.
            durability: Durability / uses left for the artifact.
            effect: Description of the artifact effect.
        """
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect
        self.type = "Artifact"

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        """Play the artifact and return its play result.

        Args:
            game_state: Current game state mapping.

        Returns:
            A dictionary describing the card played and its effect.
        """
        print(f"Drew: {self.name} ({self.type})")
        return {'card_played': self.name, 'mana_used': self.cost,
                'effect': self.effect}

    def activate_ability(self) -> Dict[str, bool]:
        """Activate the artifact ability (stub).

        Returns:
            A dictionary reporting activation success.
        """
        return {'activate': True}
