from ex4.TournamentPlatform import TournamentPlatform
from ex4.TournamentCard import TournamentCard


def main() -> None:
    try:
        print("=== DataDeck Tournament Platform ===")

        platform = TournamentPlatform()
        dragon = TournamentCard("Fire Dragon", 2, "commun", 10, 10000,
                                "dragon_001", 1200)
        wizard = TournamentCard("Ice Wizard", 3, "commun", 100, 20,
                                "wizard_001", 1150)
        print(f"{dragon.name} (ID :{dragon.card_id}):\n"
              "- Interfaces: "
              f"{dragon.get_tournament_stats().get('Interfaces', [])}\n"
              f"- Rating: {dragon.get_rank_info()}\n"
              f"- Record: {dragon.wins}-{dragon.losses}\n")
        print(f"{wizard.name} (ID :{wizard.card_id}):\n"
              "- Interfaces: "
              f"{wizard.get_tournament_stats().get('Interfaces', [])}\n"
              f"- Rating: {wizard.get_rank_info()}\n"
              f"- Record: {wizard.wins}-{wizard.losses}\n")
        print("Creating tournament match...")
        platform.register_card(dragon)
        platform.register_card(wizard)
        print("Match result: "
              f"{platform.create_match('dragon_001', 'wizard_001')}\n")

        leaderboard = platform.get_leaderboard()
        print("Tournament Leaderboard:")
        for card in leaderboard:
            print(f"{card.name} - Rating: {card.get_rank_info()} "
                  f"{card.wins}-{card.losses}")
        print(f"\nPlatform Report:\n{platform.generate_tournament_report()}\n")
        print("=== Tournament Platform Successfully Deployed! ===\n"
              "All abstract patterns working together harmoniously!")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
