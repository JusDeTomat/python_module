import math


def coordinate_system(value: tuple) -> None:
    if type(value) is str:
        old_value = value
        value = value.split(",")
        try:
            value = (int(value[0]), int(value[1]), int(value[2]))
        except ValueError as e:
            print(f"Parsing invalid coordinates: \"{old_value}\"")
            print(f"Error parsing coordinates: {e}")
            print(f"Error details - Type: {type(e).__name__}: {e.args}")
            return
        print(f"Parsing coordinates: \"{old_value}\"")
        print(f"Parsed position: {value}")
    else:
        print(f"Position created: {value}")
    formula = math.sqrt((value[0] - 0)**2 + (value[1] - 0)**2 + value[2]**2)
    print(f"Distance between (0, 0, 0) and {value}: {round(formula, 2)}")


def unpaking_tuple(arg: tuple) -> None:
    if (len(arg) == 3):
        x, y, z = arg
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")
    else:
        print("need exactly 3 arguments.")


if (__name__ == "__main__"):
    print("=== Game Coordinate System ===\n")
    coordinate_system((10, 20, 5))
    print()
    coordinate_system("3,4,0")
    print()
    coordinate_system("abc,def,ghi")
    print("\nUnpacking demonstration:")
    unpaking_tuple((3, 4, 0))
