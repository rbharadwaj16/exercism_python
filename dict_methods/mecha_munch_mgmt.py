# current_cart = {'Banana': 3, 'Apple': 2, 'Orange': 1}
# items = ('Apple', 'Apple', 'Orange', 'Apple', 'Banana')

current_cart = {"Apple": 1, "Banana": 4}
items = ("Apple", "Banana", "Orange")

for i in items:
    if i in current_cart:
        current_cart[i] += 1
    else:
        current_cart.setdefault(i, 1)

print (current_cart)