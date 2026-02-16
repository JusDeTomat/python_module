#!/usr/bin/env python3

class Plant:
    """A base class to represent a generic plant."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize the plant with name, height, and age."""
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def display(self) -> None:
        """Print the basic details of the plant."""
        print(f"Current plant: {self.name} ({self.height}cm, {self.age} days)")

    def get_height(self) -> int:
        """Return the current height of the plant."""
        return self.height

    def get_age(self) -> int:
        """Return the current age of the plant."""
        return self.age

    def set_height(self, new_h: int) -> None:
        """Update height if the value is positive."""
        if new_h <= 0:
            print(f"Invalid operation attempted: height {new_h}cm [REJECTED]")
            print("Security: Negative height rejected")
            return
        print(f"Height updated: {new_h}cm [OK]")
        self.height = new_h

    def set_age(self, new_a: int) -> None:
        """Update age if the value is positive."""
        if new_a <= 0:
            print(f"Invalid operation attempted: age {new_a} days [REJECTED]")
            print("Security: Negative age rejected")
            return
        print(f"Age updated: {new_a} days [OK]")
        self.age = new_a


class Flower(Plant):
    """A class representing a flower."""

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Initialize a flower with an additional color attribute."""
        super().__init__(name, height, age)
        self.color: str = color

    def bloom(self) -> None:
        """Print a message about the flower blooming."""
        print(f"{self.name} is blooming beautifully!")

    def display(self) -> None:
        """Print detailed info including the flower color."""
        print(f"{self.name} (Flower): {self.height}cm, {self.age} days, \
{self.color} color")


class Tree(Plant):
    """A class representing a tree with a trunk and shade."""

    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int, shade: int) -> None:
        """Initialize a tree with trunk diameter and shade area."""
        super().__init__(name, height, age)
        self.trunk_diameter: int = trunk_diameter
        self.shade: int = shade

    def produce_shade(self) -> None:
        """Display the amount of shade the tree provides."""
        print(f"{self.name} provides {self.shade} square meters of shade")

    def display(self) -> None:
        """Print detailed info including the trunk diameter."""
        print(f"{self.name} (Tree): {self.height}cm, {self.age} days, \
{self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    """A class representing a vegetable."""

    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, vitamin: str) -> None:
        """Initialize a vegetable with its harvest season and vitamin type."""
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.vitamin: str = vitamin

    def nutritional_value(self) -> None:
        """Print the vitamin content of the vegetable."""
        print(f"{self.name} is rich in vitamin {self.vitamin}")

    def display(self) -> None:
        """Print detailed info including the harvest season."""
        print(f"{self.name} (Vegetable): {self.height}cm, {self.age} days, \
{self.harvest_season} harvest")


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")
    rose: Flower = Flower("Rose", 25, 30, "red")
    tulip: Flower = Flower("Tulip", 15, 10, "yellow")
    rose.display()
    rose.bloom()
    print()

    tulip.display()
    tulip.bloom()
    print()

    oak: Tree = Tree("Oak", 500, 1825, 50, 78)
    pine: Tree = Tree("Pine", 300, 1000, 30, 40)
    oak.display()
    oak.produce_shade()
    print()

    pine.display()
    pine.produce_shade()
    print()

    tomato: Vegetable = Vegetable("Tomato", 80, 90, "summer", "C")
    carrot: Vegetable = Vegetable("Carrot", 20, 60, "autumn", "A")
    tomato.display()
    tomato.nutritional_value()
    print()

    carrot.display()
    carrot.nutritional_value()
