#!/usr/bin/env python3


class SecurePlant():
    """A class to represent a plant with private attributes."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize name, height, and age as private variables."""
        self.__name: str = name
        self.__height: int = 0
        self.__age: int = 0
        self.set_age(age)
        self.set_height(height)

    def display(self) -> None:
        """Print the plant's information."""
        print(f"Current plant: {self.__name} ({self.__height}cm, \
{self.__age} days)")

    def get_height(self) -> int:
        """Return the private height value."""
        return self.__height

    def get_age(self) -> int:
        """Return the private age value."""
        return self.__age

    def set_height(self, new_h: int) -> None:
        """Validate and update the plant's height."""
        if not isinstance(new_h, int) or new_h is None or new_h < 0:
            print(f"Invalid operation attempted: height {new_h}cm [REJECTED]")
            print("Security: Negative height rejected")
            return
        print(f"Height updated: {new_h}cm [OK]")
        self.__height = new_h

    def set_age(self, new_a: int) -> None:
        """Validate and update the plant's age."""
        if not isinstance(new_a, int) or new_a is None or new_a < 0:
            print(f"Invalid operation attempted: age {new_a} days [REJECTED]")
            print("Security: Negative age rejected")
            return
        print(f"Age updated: {new_a} days [OK]")
        self.__age = new_a


class Garden():
    """A class to store and count plant objects."""

    def __init__(self) -> None:
        """Initialize an empty plant list and counter."""
        self.lst_plant: list[SecurePlant] = []
        self.nb: int = 0

    def add_plant(self, plant: SecurePlant) -> None:
        """Add a plant instance to the garden."""
        self.lst_plant.append(plant)
        self.nb += 1


def create_plant(garden: Garden,
                 plant_data: list[tuple[str, int, int]]) -> None:
    """Create Plant objects from a list and add them to a Garden."""
    for i in range(len(plant_data)):
        print(f"Plant created: {plant_data[i][0]}")
        new_plant: SecurePlant = SecurePlant(
            plant_data[i][0],
            plant_data[i][1],
            plant_data[i][2]
        )
        garden.add_plant(new_plant)


if (__name__ == "__main__"):
    print("=== Garden Security System ===")
    plant_lst: list[tuple[str, int, int]] = [("Rose", -25, 30)]
    garden: Garden = Garden()

    create_plant(garden, plant_lst)
    first_plant: SecurePlant = garden.lst_plant[0]

    first_plant.set_height(25)
    first_plant.set_age(15)
    print()
    first_plant.set_height(20)
    print()
    first_plant.display()
