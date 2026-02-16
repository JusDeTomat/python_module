def record_spell(spell_name: str, ingredients: str) -> str:
    import alchemy.grimoire.validator as validator
    verif = validator.validate_ingredients(ingredients)
    if verif:
        return (f"Spell recorded: {spell_name} ({verif})")
    return (f"Spell rejected: {spell_name} ({verif})")
