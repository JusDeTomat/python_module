from abc import ABC, abstractmethod
from typing import Any, Dict

from ex0.Card import Card


class CardFactory(ABC):
    """Abstract factory for creating themed cards and decks."""

    @abstractmethod
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        """Create and return a creature card instance."""

    @abstractmethod
    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        """Create and return a spell card instance."""

    @abstractmethod
    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        """Create and return an artifact card instance."""

    @abstractmethod
    def create_themed_deck(self, size: int) -> Dict[str, Any]:
        """Create and return a themed deck containing several cards.

        Returns a mapping with keys like 'creature', 'spell', 'artifact'.
        """

    @abstractmethod
    def get_supported_types(self) -> Dict[str, Any]:
        """Return a structure describing supported types for this factory."""
