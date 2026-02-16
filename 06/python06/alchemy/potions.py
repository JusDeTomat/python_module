

def healing_potion():
    from .elements import create_fire, create_water
    return (f"Healing potion brewed with {create_fire()} and "
            f"{create_water()}")


def strength_potion():
    from .elements import create_fire, create_water
    return (f"Strength potion brewed with {create_water()} and "
            f"{create_fire()}")


def invisibility_potion():
    from .elements import create_water, create_air
    return (f"Invisibility potion brewed with {create_air()} "
            f"and {create_water()}")


def wisdom_potion():
    from .elements import create_water, create_air, create_earth, create_fire
    return (f"Wisdom potion brewed with all elements: {create_fire()}, "
            f"{create_water()}, {create_earth()} and {create_air()}")
