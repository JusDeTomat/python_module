from typing import Any, Dict, List

from ex3.GameStrategy import GameStrategy
from ex0.Card import Card


class AggressiveStrategy(GameStrategy):
    """Strategy that aggressively plays creatures and attacks
    low-health targets.
    """

    def execute_turn(
        self, hand: Dict[str, List[Card]], battlefield: list
    ) -> Dict[str, Any]:
        """Execute a single turn according to the aggressive strategy.

        Args:
            hand: Mapping with keys like 'creature', 'spells', 'artifacts'
                each containing lists of Card instances.
            battlefield: List of opponent targets / cards currently on the
                field.

        Returns:
            A dictionary describing actions taken this turn: cards played,
            mana, damage dealt and targets attacked.
        """
        total_mana: int = (
            sum(card.cost for card in hand.get('creature', []))
            + sum(card.cost for card in hand.get('spells', []))
            + sum(card.cost for card in hand.get('artifacts', []))
        )

        prioritize_targets: List[Card] = self.prioritize_targets(battlefield)

        if not prioritize_targets:
            total_damage: int = 0
            prioritize_targets = ["No targets to be attacked!"]
        else:
            total_damage: int = sum(
                card.cost for card in hand.get('creature', [])
            )

        pretty_targets: List[str] = [
            getattr(target, "name", str(target))
            for target in prioritize_targets
        ]
        return {
            "cards_played": (
                [card.name for card in hand.get('creature', [])]
                + [card.name for card in hand.get('spells', [])]
                + [card.name for card in hand.get('artifacts', [])]
            ),
            "mana": total_mana,
            "damage_dealt": total_damage,
            "targets_attacked": pretty_targets,
        }

    def get_strategy_name(self) -> str:
        """Return the strategy name (human readable)."""
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> List[Card]:
        """Return available targets sorted by increasing health.

        Args:
            available_targets: Iterable of target objects.

        Returns:
            A list of targets that have a 'health' attribute, sorted by health.
        """
        valid_targets: List[Card] = [
            target for target in available_targets if hasattr(target, "health")
        ]

        return sorted(valid_targets, key=lambda target: target.health)
