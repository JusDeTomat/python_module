import sys


def commande() -> None:
    arg = [x for x in sys.argv]
    print("=== Command Quest ===")
    try:
        if (len(arg) == 1):
            raise ValueError("No arguments provided!")
        print(f"Program name: {arg[0]}")
        print(f"Arguments received: {len(arg) - 1}")
        for i in range(len(arg)):
            if i != 0:
                print(f"Argument {i}: {arg[i]}")
    except ValueError as e:
        print(e)
        print(f"Program name: {arg[0]}")
    finally:
        print(f"Total arguments: {len(arg)}")


if (__name__ == "__main__"):
    commande()
