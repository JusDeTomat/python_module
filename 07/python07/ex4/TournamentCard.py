from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: str,
                 dammage: int,
                 health: int,
                 card_id: str,
                 rating: int) -> None:

        super().__init__(name, cost, rarity)
        self.wins: int = 0
        self.losses: int = 0
        self.__rating: int = rating
        self.dammage: int = dammage
        self.health: int = health
        self.card_id: str = card_id

    def play(self, game_state: dict) -> dict:
        return game_state | {
            "name": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield",
        }

    def attack(self, target) -> dict:
        target.health -= self.dammage
        if self.dammage >= target.health:
            status = True
        else:
            status = False
        return {
            "attacker": self.name,
            "target": target.name,
            "combat_resolved": status,
        }

    def defend(self, incoming_dammage: int) -> dict:
        dammage_taken: int = incoming_dammage
        self.health -= dammage_taken
        return {
            "defender": self.name,
            "still_alive": self.health > 0,
        }

    def get_combat_stats(self):
        return {"dammage": self.dammage}

    def get_rank_info(self) -> int:
        return self.__rating

    def calculate_rating(self) -> int:
        return self.__rating + self.wins * 10

    def update_losses(self) -> None:
        self.losses += 1

    def update_wins(self) -> None:
        self.wins += 1

    def get_tournament_stats(self) -> dict:
        parents: list[str] = [cls.__name__ for cls in self.__class__.__bases__]
        return {"Interfaces": parents}
