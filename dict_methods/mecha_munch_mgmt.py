
cart = {"Banana": 3, "Apple": 2, "Orange": 1, "Milk": 2}
aisle =  {
            "Banana": ["Aisle 5", False],
            "Apple": ["Aisle 4", False],
            "Orange": ["Aisle 4", False],
            "Milk": ["Aisle 2", True],
        }



for item in cart:
    if item in aisle:
        aisle[item].insert(0, cart[item])

aisle = dict(sorted(aisle.items(), reverse=True))

print(aisle)