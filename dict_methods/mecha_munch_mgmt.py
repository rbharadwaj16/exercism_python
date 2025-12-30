# current_cart = {'Banana': 3, 'Apple': 2, 'Orange': 1}
# items = ('Apple', 'Apple', 'Orange', 'Apple', 'Banana')

#current_cart = {"Apple": 1, "Banana": 4}
items = ("Apple", "Banana", "Orange")
new_cart = {}

for i in items:
    new_cart.setdefault(i, 1)

print(new_cart)