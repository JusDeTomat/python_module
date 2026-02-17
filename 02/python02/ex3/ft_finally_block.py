class GardenError(Exception):
    def __init__(self, message: str = "GardenError") -> None:
        self.message = message
        super().__init__(self.message)


class PlantError(GardenError):
    def __init__(self, message: str = "The plant is wilting!") -> None:
        super().__init__(message)


def water_plants(plant_list: list[str]) -> None:
    error: int = 0
    try:
        print("Opening watering system")
        for plante in plant_list:
            if not isinstance(plante, str) or plante == "":
                error = 1
                raise PlantError(f"Error: Cannot water {plante} - \
invalid plant!")
            print(f"Watering {plante}")
    except PlantError as e:
        print(e)
    finally:
        print("Closing watering system (cleanup)")
        if error != 1:
            print("Watering completed successfully!")


def test_watering_system() -> None:
    """
    Runs tests to demonstrate how the system handles success and errors.
    """
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    good_plants = ["Rose", "Lily", "Cactus"]
    water_plants(good_plants)

    print("\nTesting with error...")
    bad_plants = ["Sunflower", None, "Daisy"]
    water_plants(bad_plants)
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
