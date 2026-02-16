#!/usr/bin/env python3

def list_comprehension(info):
    high_scorers = [name for name, data in info.items()
                    if data["score"] > 2000]
    doubled = [data["score"] * 2 for data in info.values()]
    active = [name for name, data in info.items() if data["active"]]

    print("\n=== List Comprehension Examples ===")
    print(f"High scorers (>2000): {high_scorers}")
    print(f"Scores doubled: {doubled}")
    print(f"Active players: {active}")


def dict_comprehension(info):
    player_scores = {name: data["score"] for name, data in info["player"]
                     .items() if data["active"]}
    achiv_counts = {name: len(data["achiv"]) for name, data in info["player"]
                    .items() if data["active"]}
    dic_categories = {name: data for name, data in info["categories"].items()}
    print("\n=== Dict Comprehension Examples ===")
    print(f"Player scores: {player_scores}")
    print(f"Score categories: {dic_categories}")
    print(f"Achievement counts: {achiv_counts}")


def set_comprehension(info):
    dic_name = {name for name in info["player"].keys()}
    dic_achiv = {achiv for data in info["player"].values()
                 for achiv in data["achiv"]}
    dic_regions = {data["region"] for data in info["player"].values()
                   if data["active"]}
    print("\n=== Set Comprehension Examples ===")
    print(f"Unique players: {dic_name}")
    print(f"Unique achievements: {dic_achiv}")
    print(f"Active regions: {dic_regions}")


def combined_stat(info):
    nb_player = len(info["player"])
    nb_achiv = len({achiv for data in info["player"].values()
                    for achiv in data["achiv"]})
    nb_score = sum(data["score"] for data in info["player"].values())
    top_name = max(info["player"], key=lambda name:
                   info["player"][name]["score"])
    print("\n=== Combined Analysis ===")
    print(f"Total players: {nb_player}")
    print(f"Total unique achievements: {nb_achiv}")
    print(f"Average score: {nb_score / nb_player}")
    print(f"Top performer: {top_name} ({info["player"][top_name]['score']} \
points, {len(info["player"][top_name]["achiv"])} achievements)")


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
