from ex3.GameStrategy import GameStrategy
from ex3.CardFactory import CardFactory
from typing import Any


class GameEngine():
    def __init__(self):
        self.factory = None
        self.strategy = None
        self.turn: int = 0
        self.strategy_used: str = None
        self.total_damage: int = 0
        self.nb_created_card: int = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy
        print("Factory:", factory.__class__.__name__)
        print("Strategy:", strategy.__class__.__name__)

    def simulate_turn(self) -> dict:
        if not self.factory or not self.strategy:
            raise ValueError("Engine not configured!")

        self.turn += 1
        hand: dict[Any, Any] = self.factory.create_themed_deck(5)
        hand2: dict[Any, Any] = self.factory.create_themed_deck(5)
        self.nb_created_card = len(hand) * 3
        
        print(f"Strategy: {self.strategy.get_strategy_name()}")
        print(f"Actions: {self.strategy.execute_turn(hand, hand2)}")

    def get_engine_status(self) -> dict:
        return {
            'turns_simulated': self.turn,
            'strategy_used': self.strategy.get_strategy_name(),
            'total_dammage': self.total_damage,
            'card_created': self.nb_created_card
        }
