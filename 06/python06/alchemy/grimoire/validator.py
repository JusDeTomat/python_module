def validate_ingredients(ingredients: str) -> str:
    lst_ingredients_val = ["fire", "water", "earth", "air"]
    lst_ingredients = ingredients.split()
    for element in lst_ingredients:
        if not (element in lst_ingredients_val):
            return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"
