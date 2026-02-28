from ex3.GameStrategy import GameStrategy
from ex0.Card import Card


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        total_mana: int = sum(card.cost for card in hand.get('creature', []))
        + sum(card.cost for card in hand.get('spells', []))
        + sum(card.cost for card in hand.get('artifacts', []))

        prioritize_targets: list[Card] = self.prioritize_targets(battlefield)

        if not prioritize_targets:
            total_damage: int = 0
            prioritize_targets: list[Card] = ["No targets to be attacked!"]
        else:
            total_damage: int = sum(
                card.cost for card in hand.get('creature', [])
                )

        pretty_targets: list[str] = [
            getattr(target, "name", str(target))
            for target in prioritize_targets
        ]
        return {
            "cards_played": ([card.name for card in hand.get('creature', [])]
                             + [card.name for card in hand.get('spells', [])]
                             + [
                                card.name for card in hand.get('artifacts', [])
                             ]),
            "mana": total_mana,
            "damage_dealt": total_damage,
            "targets_attacked": pretty_targets,
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        valid_targets: list[Card] = [
            target for target in available_targets if hasattr(target, "health")
        ]

        return sorted(valid_targets, key=lambda target: target.health)
