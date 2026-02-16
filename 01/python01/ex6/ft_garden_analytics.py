#!/usr/bin/env python3

class Plant():
    """A class to manage a plant and its growth."""

    def __init__(self, name: str, height: int) -> None:
        """Initialize the plant with a name and height."""
        self.name: str = name
        self.height: int = height
        self.grows: int = 0

    def display(self) -> None:
        """Show the plant's name and current height."""
        print(f"Current plant: {self.name} ({self.height}cm)")

    def grow(self) -> None:
        """Increase the plant's height by 1cm."""
        cm = 1
        print(f"{self.name} grew {cm}cm")
        self.height += cm
        self.grows += cm

    def get_height(self) -> int:
        """Return the current height of the plant."""
        return self.height

    def set_height(self, new_h: int) -> None:
        """Update the plant's height if the value is positive."""
        if (new_h <= 0):
            print(f"Invalid operation attempted: height {new_h}cm [REJECTED]")
            print("Security: Negative height rejected")
            return
        print(f"Height updated: {new_h}cm [OK]")
        self.height = new_h


class FloweringPlant(Plant):
    """A class to represent a flower that inherits from Plant."""

    def __init__(self, name: str, height: int, color: str) -> None:
        """Initialize the flower with name, height, and color."""
        super().__init__(name, height)
        self.color: str = color

    def bloom(self) -> None:
        """Show a message when the flower blooms."""
        print(f"{self.name} is blooming beautifully!")

    def display(self) -> None:
        """Print the flower's status, including its color."""
        print(f"{self.name} (Flower): {self.height}cm, {self.color} color")


class PrizeFlower(FloweringPlant):
    """A class for award-winning flowers that have a specific prize."""

    def __init__(self, name: str, height: int, color: str, prize: int) -> None:
        """Initialize a prize-winning flower with its name, height, color, and
        prize.
        """
        super().__init__(name, height, color)
        self.prize: int = prize


class Garden():
    """A class to manage collections of plants, flowers, and prize flowers."""

    def __init__(self, name: str) -> None:
        """Initialize the garden with a name and empty plant lists."""
        self.lst_plant: list[Plant] = []
        self.lst_flower: list[FloweringPlant] = []
        self.lst_prizeflower: list[PrizeFlower] = []
        self.name: str = name
        self.plant_add: int = 0
        self.grow: int = 0
        self.nb: int = 0
        self.score: int = 0

    def add_plant(self, plant: Plant, type_plant: str) -> None:
        """Add a plant object to the correct list based on its type."""
        if (type_plant == "plant"):
            self.lst_plant.append(plant)
            print(f"Added {self.lst_plant[-1].name} to {self.name} garden")
        elif (type_plant == "flower"):
            self.lst_flower.append(plant)
            print(f"Added {self.lst_flower[-1].name} to {self.name} garden")
        elif (type_plant == "prizeflower"):
            self.lst_prizeflower.append(plant)
            print(f"Added {self.lst_prizeflower[-1].name} to {self.name} \
garden")
        else:
            return
        self.plant_add += 1

    def grow_all(self) -> None:
        """Call the grow method for every plant and flower in the garden."""
        print(f"{self.name} is helping all plants grow...")
        for element in self.lst_plant:
            element.grow()
        for element in self.lst_flower:
            element.grow()
        for element in self.lst_prizeflower:
            element.grow()
        self.grow = self.plant_add

    def calcul_score(self) -> None:
        """Calculate the total garden score based on plant rarity."""
        self.score = len(self.lst_plant) + 5 * len(self.lst_flower) + \
            10 * len(self.lst_prizeflower)


class GardenManager():
    """A class to manage and track multiple Garden objects."""

    def __init__(self) -> None:
        """Initialize the manager with an empty list of gardens."""
        self.lst_garden: list[str] = []

    def get_info(self) -> None:
        """Calculate scores and print a summary for all managed gardens."""
        line = "Garden scores -"
        i = 1
        for element in self.lst_garden:
            element.calcul_score()
            line += " " + str(element.name) + ": " + str(element.score)
            if (i < len(self.lst_garden)):
                line += ","
            i += 1
        print(line)
        print(f"Total gardens managed: {len(self.lst_garden)}")

    def add_garden(self, garden: Garden) -> None:
        """Add an existing garden instance to the management list."""
        self.lst_garden.append(garden)

    @classmethod
    def create_garden_network(cls, gardens_list: list[Garden]) -> Garden:
        """Create a new GardenManager instance and fill it with a list of
        gardens.
        """
        manage = cls()
        for garden in gardens_list:
            manage.add_garden(garden)
        return manage

    class GardenStats():
        """A nested utility class to generate reports for a garden."""

        @staticmethod
        def stats(garden) -> None:
            """Print a detailed status report for a specific garden object."""
            print(f"=== {garden.name} Garden Report ===")
            print("Plants in garden:")
            for element in garden.lst_plant:
                print(f"{element.name}: {element.height}cm")
            for element in garden.lst_flower:
                print(f"{element.name}: {element.height}cm, {element.color} \
flower (blooming)")
            for element in garden.lst_prizeflower:
                print(f"{element.name}: {element.height}cm, {element.color} \
flower (blooming), Prize points: {element.prize}")
            print("")
            print(f"Plants added: {garden.plant_add}, Total growth: \
{garden.grow}cm")
            print(f"Plant types: {len(garden.lst_plant)} regular, \
{len(garden.lst_flower)} flowering, {len(garden.lst_prizeflower)} \
prize flowers")
            print("")
            print(f"Height validation test: {garden.grow != 0}")

    def calcul_score(self) -> None:
        """Calculate the management score based on plant lists."""
        self.score = len(self.lst_plant) + 5 * len(self.lst_flower) + \
            10 * len(self.lst_prizeflower)


def main() -> None:
    print("=== Garden Management System Demo ===")
    garden = Garden("mathis")
    garden2 = Garden("Jean jack")
    manage = GardenManager.create_garden_network([garden, garden2])
    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)
    oak2 = Plant("Oak2 Tree", 100)
    rose2 = FloweringPlant("Rose2", 25, "red")
    sunflower2 = PrizeFlower("Sunflower2", 50, "yellow", 10)
    e2 = PrizeFlower("violet2", 40, "voilet", 10)
    print()
    garden.add_plant(oak, "plant")
    garden.add_plant(rose, "flower")
    garden.add_plant(sunflower, "prizeflower")
    print()
    garden.grow_all()
    print()
    garden2.add_plant(oak2, "plant")
    garden2.add_plant(rose2, "flower")
    garden2.add_plant(sunflower2, "prizeflower")
    garden2.add_plant(e2, "prizeflower")
    print()
    manage.GardenStats.stats(garden)
    manage.get_info()


if (__name__ == "__main__"):
    main()
