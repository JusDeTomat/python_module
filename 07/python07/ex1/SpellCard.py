from typing import Any, Dict, List

from ex0.Card import Card


class SpellCard(Card):
    """Concrete spell card which resolves an effect on targets."""

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        effect_type: str,
    ) -> None:
        """Create a spell card.

        Args:
            name: Card name.
            cost: Mana cost.
            rarity: Rarity string.
            effect_type: Short description of the effect.
        """
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        self.type = "Spell"

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        """Play the spell and return a description of the resolution.

        Args:
            game_state: Mapping with contextual play information.

        Returns:
            Dictionary describing the played spell and mana used.
        """
        print(f"Drew: {self.name} ({self.type})")
        return {'card_played': self.name, 'mana_used': self.cost,
                'effect': self.effect_type}

    def resolve_effect(self, targets: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Resolve spell effect over targets.

        Args:
            targets: List of target descriptors.

        Returns:
            A dictionary with effect details and the targets affected.
        """
        return {
            'effect': self.effect_type,
            'targets': targets
        }
