from abc import ABC, abstractmethod
from typing import Any, Dict


class Combatable(ABC):
    """Interface describing combat-capable entities."""

    @abstractmethod
    def attack(self, target: Any) -> Dict[str, Any]:
        """Perform an attack against the provided target.

        Args:
            target: Target object or mapping to be attacked.

        Returns:
            A dictionary describing the attack outcome.
        """

    @abstractmethod
    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        """Handle incoming damage and return defense results.

        Args:
            incoming_damage: Amount of incoming damage.

        Returns:
            A dictionary describing the defense outcome.
        """

    @abstractmethod
    def get_combat_stats(self) -> Dict[str, Any]:
        """Return a summary of combat-related stats for the entity."""
