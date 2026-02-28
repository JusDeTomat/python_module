from abc import ABC, abstractmethod
from typing import Any, Dict, List


class Magical(ABC):
    """Interface for magical capability (casting spells / channeling mana)."""

    @abstractmethod
    def cast_spell(
        self, spell_name: str, targets: List[Any]
    ) -> Dict[str, Any]:
        """Cast a spell by name against the given targets.

        Returns a dictionary describing the cast.
        """

    @abstractmethod
    def channel_mana(self, amount: int) -> Dict[str, int]:
        """Channel an amount of mana and return the resulting totals."""

    @abstractmethod
    def get_magic_stats(self) -> Dict[str, Any]:
        """Return a dictionary of magic-related statistics."""
