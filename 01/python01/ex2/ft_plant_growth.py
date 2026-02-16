#!/usr/bin/env python3

class Plant():
    """A class to represent a plant and track its daily growth."""

    def __init__(self, name: str, heigth: int, age: int) -> None:
        """Initialize the plant with a name, height, and age."""
        self.name: str = name
        self.heigth: int = heigth
        self.ages: int = age
        self.day: int = 1
        self.grows: int = 0

    def get_info(self) -> None:
        """Print the current status and growth since the last check."""
        print(f"=== Day {self.day} ===")
        print(f"{self.name}: {self.heigth}cm, {self.ages} days old")
        if (self.day != 1):
            print(f"Growth this week: +{self.grows}cm")

    def grow(self) -> None:
        """Increase the plant's height by 1cm."""
        self.heigth += 1
        self.grows += 1

    def age(self) -> None:
        """Increase age and day by 1, and trigger a growth update."""
        self.ages += 1
        self.day += 1
        self.grow()


if (__name__ == "__main__"):
    rose = Plant("rose", 25, 30)
    rose.get_info()
    for _ in range(6):
        rose.age()
    rose.get_info()
    rose.get_info()
    rose.age()
    rose.age()
    rose.get_info()
