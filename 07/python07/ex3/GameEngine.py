from typing import Any, Dict, Optional

from ex3.GameStrategy import GameStrategy
from ex3.CardFactory import CardFactory


class GameEngine:
    """Small game engine that uses a factory and a strategy to
    simulate turns.
    """

    def __init__(self) -> None:
        """Initialize engine state."""
        self.factory: Optional[CardFactory] = None
        self.strategy: Optional[GameStrategy] = None
        self.turn: int = 0
        self.strategy_used: Optional[str] = None
        self.total_damage: int = 0
        self.nb_created_card: int = 0

    def configure_engine(
        self, factory: CardFactory, strategy: GameStrategy
    ) -> None:
        """Attach a card factory and a strategy to the engine.

        Args:
            factory: CardFactory implementation used to create cards.
            strategy: GameStrategy implementation used to decide actions.
        """
        self.factory = factory
        self.strategy = strategy
        print("Factory:", factory.__class__.__name__)
        print("Strategy:", strategy.__class__.__name__)

    def simulate_turn(self) -> None:
        """Simulate a single turn using the configured factory and strategy.

        Raises:
            ValueError: If engine is not configured with both factory and
                strategy.
        """
        if not self.factory or not self.strategy:
            raise ValueError("Engine not configured!")

        self.turn += 1
        hand: Dict[str, Any] = self.factory.create_themed_deck(5)
        hand2: Dict[str, Any] = self.factory.create_themed_deck(5)
        self.nb_created_card = len(hand) * 3

        print(f"Strategy: {self.strategy.get_strategy_name()}")
        print(f"Actions: {self.strategy.execute_turn(hand, hand2)}")

    def get_engine_status(self) -> Dict[str, Any]:
        """Return a summary status of the engine."""
        return {
            'turns_simulated': self.turn,
            'strategy_used': self.strategy.get_strategy_name(),
            'total_dammage': self.total_damage,
            'card_created': self.nb_created_card,
        }
