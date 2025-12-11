list_1 = [1,2,3]
list_2 = [1,2,3]


if list_1 == list_2:
    print("EQUAL")
elif list_2 in list_1:
    print("SUPERLIST")
elif list_1 in list_2:
    print("SUBLIST")
else:
    print("UNEQUAL")