from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameEngine import GameEngine
from ex3.AggressiveStrategy import AggressiveStrategy


def main() -> None:
    """Configure a sample engine and run a turn to demonstrate patterns."""
    try:
        print("=== DataDeck Game Engine ===\n\n"
              "Configuring Fantasy Card Game...")
        engine = GameEngine()
        fantasy = FantasyCardFactory()
        strategie = AggressiveStrategy()

        engine.configure_engine(fantasy, strategie)
        print()
        print(f"Available types: {fantasy.get_supported_types()}")
        engine.simulate_turn()
        print(f"Game Report: {engine.get_engine_status()}")
        print("Abstract Factory + Strategy Pattern: Maximum flexibility "
              "achieved!")
    except Exception as e:
        print(e)


if (__name__ == "__main__"):
    main()
