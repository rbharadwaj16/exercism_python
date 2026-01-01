"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    for i in items_to_add:
        if i in current_cart:
            current_cart[i] += 1
        else:
            current_cart.setdefault(i, 1)
        
    return(current_cart)


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    new_cart = {}
    for i in notes:
        new_cart.setdefault(i, 1)

    return(new_cart)


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """

    for recipe_name, updated_ingredients in recipe_updates:
        ideas[recipe_name] = updated_ingredients
    return ideas


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    return(dict(sorted(cart.items())))


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    fulfillment_cart = {}
    for item in cart:
        fulfillment_cart[item] = [cart[item]] + aisle_mapping[item]
    return dict(sorted(fulfillment_cart.items(), reverse=True))

def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """

    updated_inventory = {}
    
    # Include all items from store_inventory
    for item in store_inventory:
        # Create a copy to avoid modifying the original
        updated_item = store_inventory[item].copy()
        
        # If item is in fulfillment cart, update the quantity
        if item in fulfillment_cart:
            delta = updated_item[0] - fulfillment_cart[item][0]
            
            if delta == 0:
                updated_item[0] = 'Out of Stock'
            else:
                updated_item[0] = delta
        
        updated_inventory[item] = updated_item
    
    return updated_inventory
