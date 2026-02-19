import sys


def parsing(arg: list) -> dict:
    """Parse tokens into a nested inventory dict.

    Supported token formats:
    - name:qty
    - name:type:qty:value
    Malformed tokens are ignored with a printed warning.
    """
    inv = {}
    for e in arg:
        if not e:
            continue
        parts = e.split(":")
        if len(parts) == 4:
            name, typ, qty, val = parts
            try:
                inv.update({name: {'type': typ, 'quantity': int(qty),
                                   'value': int(val)}})
            except ValueError:
                print(f"Ignoring malformed token (bad numbers): {e}")
        elif len(parts) == 2:
            name, qty = parts
            try:
                inv.update({name: {'type': 'unknown',
                                   'quantity': int(qty), 'value': 0}})
            except ValueError:
                print(f"Ignoring malformed token (bad number): {e}")
        else:
            print(f"Ignoring malformed token: {e}")
    return inv


def inventory_system(inv: dict) -> None:
    total = 0
    inv_key = inv.keys()
    for e in inv_key:
        total += inv[e]['quantity']
    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {total}")
    print(f"Unique item types: {len(inv_key)}")


def current_inventory(reel_inv: dict) -> None:
    print("\n=== Current Inventory ===")
    inv = reel_inv.copy()
    total = 0
    inv_key = inv.keys()
    for e in inv_key:
        total += inv[e]['quantity']
    if total == 0:
        print("Inventory is empty.")
        return
    sorted_items = sorted(inv.items(), key=lambda x: x[1]['quantity'],
                          reverse=True)
    for name, meta in sorted_items:
        qty = meta['quantity']
        percentage = (qty / total) * 100
        if qty == 1:
            print(f"{name}: {qty} unit ({percentage:.1f}%)")
        else:
            print(f"{name}: {qty} units ({percentage:.1f}%)")


def inventory_stat(inv: dict) -> None:
    inv_key = list(inv.keys())
    if not inv_key:
        print("\n=== Inventory Statistics ===")
        print("No items to analyze.")
        return
    quantities = [meta['quantity'] for meta in inv.values()]
    inv_min = min(quantities)
    inv_max = max(quantities)
    print("\n=== Inventory Statistics ===")
    for e in inv_key:
        if inv[e]['quantity'] == inv_max:
            if inv_max == 1:
                print(f"Most abundant: {e} ({inv_max} unit)")
            else:
                print(f"Most abundant: {e} ({inv_max} units)")
            break
    for e in inv_key:
        if inv[e]['quantity'] == inv_min:
            if inv_min == 1:
                print(f"Least abundant: {e} ({inv_min} unit)")
            else:
                print(f"Least abundant: {e} ({inv_min} units)")
            break


def inventory_categories(inv: dict) -> None:
    inv_key = inv.keys()
    moderate = {}
    scarce = {}
    print("\n=== Item Categories ===")
    for e in inv_key:
        if inv[e]['quantity'] >= 5:
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
        if inv[e]['quantity'] <= 1:
            suggestion.append(e)
    print(f"Restock needed: {suggestion}")


def demo(inv: dict, item: str) -> None:
    key = []
    value = []
    print("\n=== Dictionary Properties Demo ===")
    for k, v in inv.items():
        key.append(k)
        value.append(v['quantity'])
    print(f"Dictionary keys: {', '.join(key)}")
    print(f"Dictionary values: {', '.join(str(v) for v in value)}")
    print(f"Sample lookup - '{item}' in inventory: {item in inv}")


if (__name__ == "__main__"):
    arg = [x for x in sys.argv[1:]]
    inv = parsing(arg)
    inventory_system(inv)
    current_inventory(inv)
    inventory_stat(inv)
    inventory_categories(inv)
    suggestion_item(inv)
    demo(inv, 'sword')
