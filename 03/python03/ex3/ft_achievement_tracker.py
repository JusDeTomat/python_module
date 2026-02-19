def achievement_tracker(lst_player: list) -> None:
    for name, e in lst_player:
        print(f"Player {name} achievements: {e}")


def achievement_analytics(lst_player: list) -> None:
    union_lst = set()
    same_lst = set()
    rare_lst = set()
    same_lst = same_lst | lst_player[0][1]
    for name, e in lst_player:
        rare_lst = e - union_lst | rare_lst - e
        union_lst = union_lst | e
        same_lst = e & same_lst
    print(f"All unique achievements: {union_lst}")
    print(f"Total unique achievements: {len(union_lst)}\n")
    print(f"Common to all players: {same_lst}")
    print(f"Rare achievements (1 player): {rare_lst}\n")


def versus(player1: tuple, player2: tuple) -> None:
    same_lst = set()
    player1_lst = set()
    player2_lst = set()
    same_lst = player1[1]
    same_lst = player2[1] & same_lst
    player1_lst = player1[1] - player2[1]
    player2_lst = player2[1] - player1[1]
    print(f"{player1[0]} vs {player2[0]} common: {same_lst}")
    print(f"{player1[0]} unique: {player1_lst}")
    print(f"{player2[0]} unique: {player2_lst}")


if (__name__ == "__main__"):
    lst = [
        ("alice",
         {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}),
        ("bob", {'first_kill', 'level_10', 'boss_slayer', 'collector'}),
        ("charlie",
         {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
          'perfectionist'})]
    print("=== Achievement Tracker System ===\n")
    achievement_tracker(lst)
    print("\n=== Achievement Analytics ===")
    achievement_analytics(lst)
    versus(lst[0], lst[1])
