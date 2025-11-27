
colors = ["blue", "grey", "brown"]

black = 0
brown = 1
red = 2
orange = 3
yellow = 4
green = 5
blue = 6
violet = 7
grey = 8
white = 9


multiplier = globals()[colors[-1]]

str = ""
for i in range(multiplier):
    str += "0"


if str.endswith("000000000"):
    print(f'{globals()[colors[0]]}{globals()[colors[1]]} gigaohms')  
elif str.endswith("000000"):
    print(f'{globals()[colors[0]]}{globals()[colors[1]]} megaohms')
elif str.endswith("000"):
    print(f'{globals()[colors[0]]}{globals()[colors[1]]} kiloohms')
elif str.endswith("00"):
    print(f'{globals()[colors[0]]}{globals()[colors[1]]} {str} ohms')
elif str.endswith("0"):
    print(f'{globals()[colors[0]]}{globals()[colors[1]]} ohms')




