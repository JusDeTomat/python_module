def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return list(sorted(
        artifacts, key=lambda x: x.get("power", 0), reverse=True
    ))


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(
        lambda x: x.get("power", min_power - 1) >= min_power, mages
        ))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(
        lambda x: "*" + x + "*", spells
        ))


def mage_stats(mages: list[dict]) -> dict:
    lst_power = list(map(lambda x: x.get("power", 0), mages))
    avg = sum(lst_power) / len(mages)
    return {
        'max_power': max(lst_power),
        'min_power': min(lst_power),
        'avg_power': round(avg, 2)
        }


def main() -> None:
    lst = [
        {
            "name": "spell_1",
            "power": 98
        },
        {
            "name": "spell_2",
            "power": 45
        }
    ]
    lst_str = ["fireball", "heal", "shield"]
    print("Testing artifact sorter...")
    sort = artifact_sorter(lst)
    print(f"{sort[0]['name']}({sort[0]['power']} power) comes \
before {sort[1]['name']}({sort[1]['power']} power)\n")

    print("Testing spell transformer...")
    transformer = spell_transformer(lst_str)
    print(transformer[0], transformer[1], transformer[2])

    print("\nTesting power filter")
    min_power = 50
    power = power_filter(lst, min_power)
    print(f"power > {min_power}: {power}\n")

    print("Testing mage stats")
    mage = mage_stats(lst)
    print(f" - max power: {mage['max_power']}\n - min power:\
 {mage['min_power']}\n - average: {mage['avg_power']}")


if (__name__ == "__main__"):
    main()
