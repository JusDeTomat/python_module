#!/usr/bin/env python3

class Plant:
    """A class to represent a plant with basic status tracking."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize the plant with a name, height, and age."""
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def display(self) -> None:
        """Print the plant's current details to the console."""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    rose: Plant = Plant("Rose", 25, 30)
    sunflower: Plant = Plant("Sunflower", 80, 45)
    cactus: Plant = Plant("Cactus", 15, 120)

    rose.display()
    sunflower.display()
    cactus.display()
