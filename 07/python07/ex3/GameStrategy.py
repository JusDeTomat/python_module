from abc import ABC, abstractmethod
from typing import Any, Dict, List


class GameStrategy(ABC):
    """Abstract strategy for deciding actions each turn."""

    @abstractmethod
    def execute_turn(
        self, hand: Any, battlefield: List[Any]
    ) -> Dict[str, Any]:
        """Execute a turn and return a summary of actions taken."""

    @abstractmethod
    def get_strategy_name(self) -> str:
        """Return the strategy name as a human-readable string."""

    @abstractmethod
    def prioritize_targets(self, available_targets: List[Any]) -> List[Any]:
        """Return a list of prioritized targets from available_targets."""
