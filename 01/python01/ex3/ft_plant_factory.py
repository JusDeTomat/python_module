class Plant():
    """A class to represent a plant and track its growth over time."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize the plant with its name, height, and age."""
        self.name: str = name
        self.height: int = height
        self.age: int = age
        self.day: int = 1
        self.grows: int = 0

    def get_info(self) -> None:
        """Display the current status and recent growth of the plant."""
        print(f"=== Day {self.day} ===")
        print(f"{self.name}: {self.height}cm, {self.age} days old")
        if (self.day != 1):
            print(f"Growth this week: +{self.grows}cm")
            self.grows = 0

    def grow(self) -> None:
        """Increase the height of the plant by 1cm."""
        self.height += 1
        self.grows += 1

    def age_one_day(self) -> None:
        """Advance the plant's age and day, and trigger growth."""
        self.age += 1
        self.day += 1
        self.grow()


class Garden():
    """A class to hold a collection of plant objects."""

    def __init__(self) -> None:
        """Initialize an empty list of plants and a counter."""
        self.lst_plant: list[Plant] = []
        self.nb: int = 0

    def add_plant(self, plant: Plant) -> None:
        """Add a plant instance to the garden's list."""
        self.lst_plant.append(plant)
        self.nb += 1


def create_plant(garden: Garden,
                 plant_data: list[tuple[str, int, int]]) -> None:
    """Create multiple Plant objects from a list and add them to a Garden."""
    for i in range(len(plant_data)):
        new_plant = Plant(plant_data[i][0], plant_data[i][1], plant_data[i][2])
        garden.add_plant(new_plant)
        print(f"Created: {plant_data[i][0]} ({plant_data[i][1]}cm, \
{plant_data[i][2]} days)")


if (__name__ == "__main__"):
    print("=== Plant Factory Output ===")
    plant_lst: list[tuple[str, int, int]] = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]

    my_garden: Garden = Garden()
    create_plant(my_garden, plant_lst)
    print(f"\nTotal plants created: {my_garden.nb}")
