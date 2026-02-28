from typing import Any, Dict, Optional
import random

from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    """Platform to register cards and run tournament matches."""

    def __init__(self) -> None:
        """Initialize a new tournament platform instance."""
        self.lst_card: list[TournamentCard] = []
        self.player_map: dict[str, TournamentCard] = {
            p.card_id: p for p in self.lst_card
        }
        self.match_count: int = 0
        self.activity: str = "active"

    def register_card(self, card: TournamentCard) -> str:
        """Register a new card on the platform and return its id.

        Args:
            card: TournamentCard instance to register.

        Returns:
            The registered card's id.
        """
        self.lst_card.append(card)
        self.player_map[card.card_id] = card
        return card.card_id

    def create_match(self, card1_id: str, card2_id: str) -> Dict[str, Any]:
        """Run a match between two registered cards and return the result.

        Args:
            card1_id: ID of the first participant.
            card2_id: ID of the second participant.

        Returns:
            A dictionary containing the winner, loser and their ratings.

        Raises:
            ValueError: If either ID is not found on the platform.
        """
        self.match_count += 1
        card1: Optional[TournamentCard] = self.player_map.get(card1_id)
        card2: Optional[TournamentCard] = self.player_map.get(card2_id)
        if not card1 or not card2:
            raise ValueError("ID not found")
        first_player: TournamentCard = random.choice(seq=[card1, card2])
        second_player: TournamentCard = (
            card2 if first_player == card1 else card1
        )
        while first_player.health > 0 and second_player.health > 0:
            first_player.attack(second_player)
            second_player.defend(first_player.dammage)
            if second_player.health > 0:
                second_player.attack(first_player)
                first_player.defend(second_player.dammage)
        if first_player.health > 0:
            winner: TournamentCard = first_player
            loser: TournamentCard = second_player
        else:
            winner: TournamentCard = second_player
            loser: TournamentCard = first_player
        winner.update_wins()
        loser.update_losses()
        return {
            "winner": winner.card_id,
            "loser": loser.card_id,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating(),
        }

    def get_leaderboard(self) -> list:
        """Return the leaderboard sorted by calculated rating (desc)."""
        return sorted(
            self.lst_card,
            key=lambda target: target.calculate_rating(),
            reverse=True,
        )

    def generate_tournament_report(self) -> Dict[str, Any]:
        """Generate a simple report about the tournament platform."""
        avg_rating = sum(p.calculate_rating() for p in self.lst_card) / len(
            self.lst_card
        )
        return {
            "total_cards": len(self.lst_card),
            "matches_played": self.match_count,
            "avg_rating": avg_rating,
            "platform_status": self.activity,
        }
