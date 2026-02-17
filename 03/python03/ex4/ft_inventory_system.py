import sys


def parcing(arg: list) -> dict:
    inv = {}
    for e in arg:
        key, value = e.split(':')
        inv.update({key: int(value)})
    return inv


def inventory_systeme(inv: dict) -> None:
    total = 0
    inv_key = inv.keys()
    for e in inv_key:
        total += inv[e]
    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {total}")
    print(f"Unique item types: {len(inv_key)}")


def current_inventory(reel_inv: dict) -> None:
    print("\n=== Current Inventory ===")
    inv = reel_inv.copy()
    total = 0
    inv_key = inv.keys()
    for e in inv_key:
        total += inv[e]
    sorted_items = sorted(inv.items(), key=lambda x: x[1], reverse=True)
    for name, qty in sorted_items:
        percentage = (qty / total) * 100
        if (qty <= 1):
            print(f"{name}: {qty} unit ({percentage:.1f}%)")
        else:
            print(f"{name}: {qty} units ({percentage:.1f}%)")


def inventory_stat(inv: dict) -> None:
    inv_key = inv.keys()
    inv_value = inv.values()
    inv_min = 0
    inv_max = 0
    if (len(inv_value) >= 1):
        inv_min = min(inv_value)
        inv_max = max(inv_value)
    print("\n=== Inventory Statistics ===")
    for e in inv_key:
        if (inv[e] == inv_max):
            if (inv[e] == 1):
                print(f"Most abundant: {e} ({inv_max} unit)")
                break
            else:
                print(f"Most abundant: {e} ({inv_max} units)")
                break
    for e in inv_key:
        if (inv[e] == inv_min):
            if (inv[e] == 1):
                print(f"Least abundant: {e} ({inv_min} unit)")
                break
            else:
                print(f"Least abundant: {e} ({inv_min} units)")
                break


def inventory_categories(inv: dict) -> None:
    inv_key = inv.keys()
    moderate = {}
    scarce = {}
    print("\n=== Item Categories ===")
    for e in inv_key:
        if (inv[e] >= 5):
            moderate[e] = inv[e]
        else:
            scarce[e] = inv[e]
    if (len(moderate) > 0):
        print(f"Moderate: {moderate}")
    if (len(scarce) > 0):
        print(f"Scarce: {scarce}")


def suggestion_item(inv: dict) -> None:
    inv_key = inv.keys()
    suggestion = []
    print("\n=== Management Suggestions ===")
    for e in inv_key:
        if (inv[e] <= 1):
            suggestion.append(e)
    print(f"Restock needed: {suggestion}")


def demo(inv: dict, item: str) -> None:
    key = []
    value = []
    print("\n=== Dictionary Properties Demo ===")
    for k, v in inv.items():
        key.append(k)
        value.append(v)
    print(f"Dictionary keys: {key}")
    print(f"Dictionary values: {value}")
    print(f"Sample lookup - '{item}' in inventory: {inv.get(item) == 1}")


if (__name__ == "__main__"):
    arg = [x for x in sys.argv[1:]]
    inv = parcing(arg)
    inventory_systeme(inv)
    current_inventory(inv)
    inventory_stat(inv)
    inventory_categories(inv)
    suggestion_item(inv)
    demo(inv, 'sword')
