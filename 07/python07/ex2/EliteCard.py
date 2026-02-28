from typing import Any, Dict, List

from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex0.Card import Card


class EliteCard(Card, Combatable, Magical):
    """A card that combines combat and magical interfaces.

    This class implements both the Combatable and Magical interfaces and
    provides a richer set of behaviors (attack, defend, cast spells, etc.).
    """

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        damage: int,
        health: int,
        combat_type: str,
    ) -> None:
        """Initialize an EliteCard.

        Args:
            name: Card name.
            cost: Mana cost.
            rarity: Rarity string.
            damage: Damage dealt when attacking.
            health: Health points.
            combat_type: Combat style (e.g. 'melee', 'ranged').
        """
        self.name = name
        self.cost = cost
        self.rarity = rarity
        self.dommage = damage
        self.health = health
        self.combat_type = combat_type
        self.type = "EliteCard"

    def cast_spell(
        self, spell_name: str, targets: List[Any]
    ) -> Dict[str, Any]:
        """Cast a spell and return a description of the cast action."""
        return {
            'caster': self.name,
            'spell': spell_name,
            'target': targets,
            'mana_used': self.cost,
        }

    def channel_mana(self, amount: int) -> Dict[str, int]:
        """Channel additional mana and report totals."""
        return {
            'channeled': amount,
            'total_mana': self.cost + amount,
        }

    def get_magic_stats(self) -> Dict[str, int]:
        """Return magic-related statistics for this card."""
        return {'mana': self.cost}

    def attack(self, target: Any) -> Dict[str, Any]:
        """Attack a target described as a mapping-like object.

        Args:
            target: Mapping with at least 'hp' and 'name' keys.

        Returns:
            A dictionary describing the attack result.
        """
        hp_target = target.get('hp', 0)
        name_target = target.get('name', 'enemy')
        target['hp'] = hp_target - self.dommage
        return {
            'attacker': self.name,
            'target': name_target,
            'damage': self.dommage,
            'combat_type': self.combat_type,
        }

    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        """Defend against incoming damage and report the result."""
        return {
            'defender': self.name,
            'damage_taken': incoming_damage - self.dommage // 2,
            'domage_blocked': self.dommage // 2,
            'still_alive': (
                self.health - (incoming_damage - self.dommage / 2)
            ) > 0,
        }

    def get_combat_stats(self) -> Dict[str, int]:
        """Return combat statistics for this card."""
        return {
            'dommage': self.dommage,
        }

    def play(self, game_state: Dict[str, Any]) -> None:
        """Execute the card's play behavior (combat + magic phases).

        The method prints results and does not currently return a value.
        """
        print(
            f"Playing {self.name} ({self.type}):\n\n"
            "Combat phase:\n"
            f"Attack result: {self.attack(game_state.get('ar', {}))}\n"
            f"Defense result: {self.defend(game_state.get('dr', 0))}\n"
        )
        result_cast_spell = self.cast_spell(
            game_state.get('scs', 'spell'), game_state.get('sce', [])
        )
        print(
            "Magic phase:\n"
            f"Spell cast: {result_cast_spell}\n"
            f"Mana channel: {self.channel_mana(game_state.get('mc', 0))}\n"
        )
