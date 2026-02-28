from abc import abstractmethod, ABC


class Rankable(ABC):
    """Interface for objects that can be ranked / rated."""

    @abstractmethod
    def calculate_rating(self) -> int:
        """Compute and return the current rating for the object."""

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        """Update internal state for additional wins."""

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        """Update internal state for additional losses."""

    @abstractmethod
    def get_rank_info(self) -> int:
        """Return a compact rank/info integer (e.g. ELO or similar)."""
