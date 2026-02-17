class GardenError(Exception):
    def __init__(self, message: str = "GardenError") -> None:
        self.message: str = message
        super().__init__(self.message)


class PlantError(GardenError):
    def __init__(self, message: str = "The plant is wilting!") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Not enough water in the tank!") -> None:
        super().__init__(message)


class HealthError(GardenError):
    def __init__(self, message: str = "not good value!") -> None:
        super().__init__(message)


class Plant():
    def __init__(self, name, water, sun):
        assert name == str(name), "name need to be in type str"
        self.name = name
        self.water = water
        self.sun = sun


class GardenManager():
    def __init__(self, tank):
        self.lst_plant = []
        self.tank = tank

    def add_plant(self, lst_plant):
        try:
            for plant in lst_plant:
                if (plant.name == ""):
                    raise PlantError("Plant name cannot be empty!")
                print(f"Added {plant.name} successfully")
                self.lst_plant.append(plant)
        except PlantError as e:
            print(f"Error adding plant: {e}")
        finally:
            print()

    def water_plant(self):
        try:
            print("Opening watering system")
            for plant in self.lst_plant:
                if (self.tank <= 0):
                    raise WaterError("No more wather to wather")
                print(f"Watering {plant.name} - success")
                self.tank -= 1
        except WaterError as e:
            print(e)
        finally:
            print("Closing watering system (cleanup)\n")

    def modify_water(self, water):
        try:
            if (self.tank - water <= 0):
                raise WaterError("Caught GardenError: Not enough water in \
tank")
            self.tank = water
        except WaterError as e:
            print(e)
        finally:
            print("System recovered and continuing...\n")

    def check_plant_health(self):
        try:
            for plant in self.lst_plant:
                if (plant.water > 10):
                    raise HealthError(f"Water level {plant.water} is too high \
(max 10)")
                if (plant.water < 1):
                    raise HealthError(f"Water level {plant.water} is too low \
(min 1)")
                if (plant.sun > 12):
                    raise HealthError(f"Sunlight hours  {plant.sun} is too \
high (max 12)")
                if (plant.sun < 2):
                    raise HealthError(f"Sunlight hours  {plant.sun} is too \
low (min 2)")
                print(f"{plant.name}: healthy (water: {plant.water}, sun: \
{plant.sun})")

        except HealthError as e:
            print(f"Error checking {plant.name}: {e}")
        finally:
            print()


def test_garden_management():
    print("=== Garden Management System ===")
    p1 = Plant("tomato", 5, 8)
    p2 = Plant("lettuce", 15, 5)
    p3 = Plant("", 1, 1)
    garden = GardenManager(2)
    print("Adding plants to garden...")
    garden.add_plant([p1, p2, p3])
    print("Watering plants...")
    garden.water_plant()
    print("Checking plant health...")
    garden.check_plant_health()
    print("Testing error recovery...")
    garden.modify_water(100)
    print("Garden management system test complete!")


if (__name__ == "__main__"):
    test_garden_management()
