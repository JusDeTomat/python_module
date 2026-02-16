#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self,
                 message: str = "plant need to be str and water to") -> None:
        self.message = message
        super().__init__(self.message)


class PlantError(GardenError):
    def __init__(self) -> None:
        super().__init__("The plant is wilting!")


class WaterError(GardenError):
    def __init__(self) -> None:
        super().__init__("Not enough water in the tank!")


def test_error(plant: str, water: str):
    """this fonction test all costom error"""
    garden: list[str] = ["tomate"]
    try:
        if isinstance(plant, str) and isinstance(water, str):
            raise GardenError()
        try:
            if (plant not in garden):
                raise PlantError()
        except PlantError as e:
            print(f"Caught PlantError: {e}")
        try:
            if (water != "water"):
                raise WaterError()
        except WaterError as e:
            print(f"Caught WaterError: {e}")
    except GardenError as e:
        print(f"Caught GardenError:{e}")


if (__name__ == "__main__"):
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")
    test_error(12, "water")
    print()
    test_error("moi", "water")
    print()
    print("Testing WaterError...")
    test_error("tomate", "sun")
    print()
    print("Testing catching all garden errors...")
    test_error("moi", "sun")
    print("\nAll custom error types work correctly!")
