def list_comprehension(info):
    high_scorers = [name for name, data in info.items()
                    if data.get("score", 0) > 2000]
    doubled = [data.get("score", 0) * 2 for data in info.values()]
    active = [name for name, data in info.items() if data.get("active", False)]

    print("\n=== List Comprehension Examples ===")
    print(f"High scorers (>2000): {high_scorers}")
    print(f"Scores doubled: {doubled}")
    print(f"Active players: {active}")


def dict_comprehension(info):
    player_scores = {name: data.get("score", 0)
                     for name, data in info["player"].items()
                     if data.get("active", False)}
    achiv_counts = {name: len(data.get("achiv", set()))
                    for name, data in info["player"].items()
                    if data.get("active", False)}
    dic_categories = {name: data for name, data in info["categories"].items()}
    print("\n=== Dict Comprehension Examples ===")
    print(f"Player scores: {player_scores}")
    print(f"Score categories: {dic_categories}")
    print(f"Achievement counts: {achiv_counts}")


def set_comprehension(info):
    dic_name = {name for name in info["player"].keys()}
    dic_achiv = {achiv for data in info["player"].values()
                 for achiv in data.get("achiv", set())}
    dic_regions = {data["region"] for data in info["player"].values()
                   if data.get("active", False)}
    print("\n=== Set Comprehension Examples ===")
    print(f"Unique players: {dic_name}")
    print(f"Unique achievements: {dic_achiv}")
    print(f"Active regions: {dic_regions}")


def combined_stat(info):
    nb_player = len(info["player"])
    nb_achiv = len({achiv for data in info["player"].values()
                    for achiv in data.get("achiv", set())})
    nb_score = sum(data.get("score", 0) for data in info["player"].values())
    top_name = max(info["player"].keys(),
                   key=lambda name: info["player"][name].get("score", 0))
    print("\n=== Combined Analysis ===")
    print(f"Total players: {nb_player}")
    print(f"Total unique achievements: {nb_achiv}")
    print(f"Average score: {nb_score / nb_player}")
    top_score = info["player"][top_name].get("score", 0)
    top_achiv_count = len(info["player"][top_name].get("achiv", set()))
    print(f"Top performer: {top_name} ({top_score} points, "
          f"{top_achiv_count} achievements)")


if (__name__ == "__main__"):
    dico = {
        "player": {
            "alice": {
                "score": 2300, "active": True,
                "achiv": {"first_kill", "level_10", "boss_slayer",
                          "marathon_runner"},
                "region": "east"
            },
            "bob": {
                "score": 1800, "active": True,
                "achiv": {"first_kill", "level_10"},
                "region": "north"
            },
            "charlie": {
                "score": 2150, "active": True,
                "achiv": {"first_kill", "level_10", "boss_slayer"},
                "region": "central"
            },
            "diana": {
                "score": 2050, "active": False,
                "achiv": {"first_kill", "level_10", "legendary_loot"},
                "region": "south"
            },
            "ethan": {
                "score": 3100, "active": True,
                "achiv": {"first_kill", "level_10", "boss_slayer",
                          "top_1_global"},
                "region": "west"
            },
            "fiona": {
                "score": 950, "active": True,
                "achiv": {"first_kill"},
                "region": "east"
            },
            "george": {
                "score": 1400, "active": False,
                "achiv": {"level_10", "collector"},
                "region": "north"
            },
            "hannah": {
                "score": 2750, "active": True,
                "achiv": {"first_kill", "level_10", "boss_slayer",
                          "speedrunner"},
                "region": "south"
            }
        },
        "categories": {
            "elite": 5,
            "pro": 4,
            "high": 3,
            "medium": 2,
            "low": 1,
            "newbie": 0
        }
    }
    print("=== Game Analytics Dashboard ===")
    list_comprehension(dico["player"])
    dict_comprehension(dico)
    set_comprehension(dico)
    combined_stat(dico)
