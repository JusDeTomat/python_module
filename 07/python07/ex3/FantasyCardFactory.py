from typing import Any, Dict

from ex3.CardFactory import CardFactory
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from random import randint, choice


class FantasyCardFactory(CardFactory):
    """Concrete CardFactory that generates fantasy-themed cards."""

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        """Create and return a randomized creature card."""
        creatures = [
            "Ebony Dragon",
            "Lunar Sylph",
            "Crystal Golem",
            "Marsh Hydra",
            "Cinder Phoenix",
            "Shadow Wolf",
            "Deepsea Titan",
            "Mist Fairy",
            "Runic Minotaur",
            "Astral Serpent",
        ]
        rarities = [
            "Common",
            "Uncommon",
            "Rare",
            "Epic",
            "Legendary",
            "Mythic",
            "Ancient",
            "Divine",
        ]
        return CreatureCard(
            choice(creatures),
            randint(0, 20),
            choice(rarities),
            randint(1, 30),
            randint(50, 1000),
        )

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        """Create and return a randomized spell card."""
        spells = [
            "Arcane Nova",
            "Veil of Invisibility",
            "Mana Storm",
            "Seal of Stasis",
            "Solar Invocation",
            "Curse of the Abyss",
            "Runic Explosion",
            "Spirit Bond",
            "Meteor Shower",
            "Soul Transfer",
        ]
        rarities = [
            "Common",
            "Uncommon",
            "Rare",
            "Epic",
            "Legendary",
            "Mythic",
            "Ancient",
            "Divine",
        ]
        effect_types = [
            "Damage",
            "Heal",
            "Shield",
            "Buff",
            "Debuff",
            "Poison",
            "Burn",
            "Freeze",
            "Stun",
            "Silence",
            "Lifesteal",
            "Summon",
            "Teleport",
            "Mana Restore",
            "Curse",
        ]
        return SpellCard(
            choice(spells),
            randint(0, 20),
            choice(rarities),
            choice(effect_types),
        )

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        """Create and return a randomized artifact card."""
        artifacts = [
            "Orb of the Ancients",
            "Blade of the Void",
            "Crown of Aeons",
            "Forbidden Grimoire",
            "Amulet of the Guardian",
            "Scepter of Dawn",
            "Resurrection Stone",
            "Mirror of Truths",
            "Ring of the Void",
            "Heart of the Titan",
        ]
        rarities = [
            "Common",
            "Uncommon",
            "Rare",
            "Epic",
            "Legendary",
            "Mythic",
            "Ancient",
            "Divine",
        ]
        effect = [
            "Damage",
            "Heal",
            "Shield",
            "Buff",
            "Debuff",
            "Poison",
            "Burn",
            "Freeze",
            "Stun",
            "Silence",
            "Lifesteal",
            "Summon",
            "Teleport",
            "Mana Restore",
            "Curse",
        ]
        return ArtifactCard(
            choice(artifacts),
            randint(0, 20),
            choice(rarities),
            randint(0, 30),
            choice(effect),
        )

    def create_themed_deck(self, size: int) -> Dict[str, Any]:
        """Return a themed deck mapping containing lists of cards.

        The returned dict contains keys 'creature', 'spell' and 'artifact'.
        """
        lstc, lsta, lsts = [], [], []
        for _ in range(size):
            lstc.append(self.create_creature())
            lsta.append(self.create_spell())
            lsts.append(self.create_artifact())
        return {
            'creature': lstc,
            'spell': lsts,
            'artifact': lsta,
        }

    def get_supported_types(self) -> Dict[str, Any]:
        """Return a small example mapping of supported types."""
        return {
            'creatures': ['dragon', 'goblin'],
            'spells': ['fireball'],
            'artifacts': ['mana_ring'],
        }
