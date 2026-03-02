from typing import Any, Dict

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    """A card used in tournament simulations.

    Implements combat and ranking interfaces used by the tournament
    platform.
    """

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        dammage: int,
        health: int,
        card_id: str,
        rating: int,
    ) -> None:
        """Initialize a TournamentCard.
        Args:
            name: Card name.
            cost: Mana cost.
            rarity: Rarity string.
            dammage: Damage dealt when attacking (note: spelled 'dammage'
                in this codebase).
            health: Health points.
            card_id: Unique identifier used by the tournament platform.
            rating: Initial rating value (e.g. ELO-like score).
        """

        super().__init__(name, cost, rarity)
        self.wins: int = 0
        self.losses: int = 0
        self.__rating: int = rating
        self.dammage: int = dammage
        self.health: int = health
        self.card_id: str = card_id

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        """Play the card by merging a small effect into the game state.

        Returns a new mapping containing the updated state keys.
        """
        return game_state | {
            "name": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield",
        }

    def attack(self, target: "TournamentCard") -> Dict[str, Any]:
        """Attack another TournamentCard instance.

        Args:
            target: The defending card instance.

        Returns:
            Dictionary indicating attacker, target and whether combat
            resolved (target died).
        """
        target.health -= self.dammage
        status = self.dammage >= target.health
        return {
            "attacker": self.name,
            "target": target.name,
            "combat_resolved": status,
        }

    def defend(self, incoming_dammage: int) -> Dict[str, Any]:
        """Apply incoming damage to this card and report survival."""
        dammage_taken: int = incoming_dammage
        self.health -= dammage_taken
        return {"defender": self.name, "still_alive": self.health > 0}

    def get_combat_stats(self) -> Dict[str, int]:
        """Return combat-related statistics for this card."""
        return {"dammage": self.dammage}

    def get_rank_info(self) -> int:
        """Return the current internal rating (compact info)."""
        return self.__rating

    def calculate_rating(self) -> int:
        """Compute a derived rating from wins and base rating."""
        return self.__rating + self.wins * 10

    def update_losses(self) -> None:
        """Increment internal loss counter."""
        self.losses += 1

    def update_wins(self) -> None:
        """Increment internal win counter."""
        self.wins += 1

    def get_tournament_stats(self) -> Dict[str, Any]:
        """Return lightweight tournament metadata for this card."""
        parents: list[str] = [cls.__name__ for cls in self.__class__.__bases__]
        return {"Interfaces": parents}
