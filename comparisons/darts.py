def score(x, y):

    distance_squared = (x ** 2) + (y ** 2) 
    r1 = 1 ** 2
    r2 = 5 ** 2
    r3 = 10 ** 2


    if distance_squared <= r1:
        return 10
    elif distance_squared <= r2:
        return 5
    elif distance_squared <= r3:
        return 1
    else:
        return 0
