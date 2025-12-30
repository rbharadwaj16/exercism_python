def update_recipes(ideas, update):
    """Update recipes with new ingredient quantities.
    
    :param ideas: dict - recipe names and their ingredient dictionaries
    :param update: tuple - tuples of (recipe_name, updated_ingredients_dict)
    :return: dict - updated recipe dictionary
    """
    for recipe_name, updated_ingredients in update:
        ideas[recipe_name] = updated_ingredients
    return ideas
