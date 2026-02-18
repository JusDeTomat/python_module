from abc import ABC, abstractmethod


class Card(ABC):
    def __init__(self, name: str, const: int, rarity: str):
        self.name = name
        self.cost = const
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        pass

    def is_playable(self, available_mana: int) -> bool:
        return available_mana > self.cost
