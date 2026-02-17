class GardenError(Exception):
    def __init__(self, message: str = "GardenError") -> None:
        self.message = message
        super().__init__(self.message)


class PlantError(GardenError):
    def __init__(self, message: str = "The plant is wilting!") -> None:
        super().__init__(message)


def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> None:
    try:
        if not (isinstance(plant_name, str) and isinstance(water_level, int)
                and isinstance(sunlight_hours, int)):
            raise PlantError("Worth input:name (str)\n      -water (int)\n    "
                             "  -sun (int)")
        if (plant_name == ""):
            raise PlantError("Plant name cannot be empty!")
        if (water_level > 10):
            raise PlantError(f"Water level {water_level} is too high (max 10)")
        if (water_level < 1):
            raise PlantError(f"Water level {water_level} is too low (min 1)")
        if (sunlight_hours > 12):
            raise PlantError(f"Sunlight hours {sunlight_hours} is too high \
(max 12)")
        if (sunlight_hours < 2):
            raise PlantError(f"Sunlight hours {sunlight_hours} is too low \
(min 2)")
        return f"Plant {plant_name} is healthy!"
    except PlantError as e:
        return f"Error: {e}"


def test_plant_checks() -> None:
    """test fonction check_plant_health"""
    print("=== Garden Plant Health Checker ===")
    print("\nTesting good values...")
    print(check_plant_health("Basilic", 5, 6))

    print("\nTesting empty plant name...")
    print(check_plant_health(None, 5, 6))

    print("\nTesting bad water level...")
    print(check_plant_health("Cactus", 15, 6))

    print("\nTesting bad sunlight hours...")
    print(check_plant_health("Cactus", 5, -8))

    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
