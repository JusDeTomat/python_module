from abc import ABC, abstractmethod
from typing import Any, Dict


class Card(ABC):
    """Abstract base class representing a generic card.

    Subclasses should implement the :meth:`play` method.
    """

    def __init__(self, name: str, const: int, rarity: str) -> None:
        """Initialize a card.

        Args:
            name: Human-readable card name.
            const: Mana cost to play the card.
            rarity: Rarity string (e.g. "Common", "Rare").
        """
        self.name: str = name
        self.cost: int = const
        self.rarity: str = rarity

    @abstractmethod
    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        """Play the card, performing its effect against the game state.

        Args:
            game_state: A mapping representing current game state.

        Returns:
            A dictionary describing the result of playing the card.
        """

    def get_card_info(self) -> Dict[str, Any]:
        """Return a serializable representation of the card.

        Returns:
            A dictionary with card metadata (name, cost, rarity, ...).
        """
        raise NotImplementedError()

    def is_playable(self, available_mana: int) -> bool:
        """Return True if the card can be played with the given mana.

        Args:
            available_mana: Amount of mana available to the player.

        Returns:
            True if available_mana is greater than the card cost.
        """
        return available_mana > self.cost
