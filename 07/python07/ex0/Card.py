import abc


class Card():
    def __init__(self, name: str, const: int, rarity: str):
        self.name = name
        self.const = const
        self.rarity = rarity

    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        pass

    def is_playable(self, available_mana: int) -> bool:
        pass
