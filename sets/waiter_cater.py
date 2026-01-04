dish = ('Ginger Glazed Tofu Cutlets', ['tofu', 'soy sauce', 'ginger', 'corn starch', 'garlic', 'brown sugar', 'sesame seeds', 'lemon juice'])


SPECIAL_INGREDIENTS = {'cream','bacon', 'garlic', 'baby scallops', 'mussels', 'baby squid', 'cashews', 'salmon fillets',
                       'filo pastry', 'almonds', 'milk', 'blue cheese', 'clams', 'shrimp', 'tomato puree', 'chocolate',
                       'honey', 'anchovy fillets', 'bulgur', 'prawns', 'parmesan cheese', 'fish', 'shelled large shrimp',
                       'gluten', 'crab legs', 'feta cheese', 'whole-milk yogurt', 'crema', 'firm tofu', 'fish stock',
                       'fresh ricotta', 'tomato paste', 'fresh cherry tomatoes', 'pork chops', 'eggs', 'greek yogurt',
                       'hazelnuts', 'pecans', 'brie cheese', 'oaxaca cheese', 'yellow onion', 'whey', 'silken tofu',
                       'toasted bread', 'parmesan', 'beef', 'tofu', 'flour', 'tomatoes', 'red onion', 'slivered almonds',
                       'strawberries', 'onions', 'pine nuts', 'cherry tomatoes', 'soy sauce', 'oyster sauce',
                       'mozzarella cheese', 'roma tomatoes', 'heavy cream', 'paneer', 'pork tenderloin', 'garlic cloves',
                       'swiss cheese', 'grilled king fish', 'ground almonds', 'tilapia', 'sprint onion', 'couscous',
                       'walnuts', 'semolina', 'yogurt', 'cotija cheese', 'oysters', 'spaghetti', 'cheddar cheese',
                       'butter', 'lobster', 'smoked tofu', 'peanuts', 'ground pork', 'fresh cherry bocconcini',
                       'pork belly', 'toasted peanuts', 'roasted peanuts'
                       }


new_dish = set(dish[1])

common = new_dish.intersection(SPECIAL_INGREDIENTS)
final = (dish[0], common)

print(type(final))

