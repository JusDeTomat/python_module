from ex3.FantasyCardFactory import FantasyCardFactory


def main():
    print("=== DataDeck Game Engine ===\n\n"
          "Configuring Fantasy Card Game...\n"
          "Factory: FantasyCardFactory\n"
          "Strategy: AggressiveStrategy")
    fantasy = FantasyCardFactory()
    print(f"Available types: {fantasy.get_supported_types()}")


if (__name__ == "__main__"):
    main()
