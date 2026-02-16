def ft_plant_age():
    day = int(input("Enter plant age in days: "))
    if (day > 60):
        print("Plant is ready to harvest!")
        return
    print("Plant needs more time to grow.")
