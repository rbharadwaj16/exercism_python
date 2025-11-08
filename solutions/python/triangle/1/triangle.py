def is_triangle(sides):

    if (sides[0] or sides[1] or sides[2]) <= 0:
        return False
    elif sides[0] + sides[1] <= sides[2]:
        return False
    elif sides[1] + sides[2] <= sides[0]:
        return False
    elif sides[0] + sides[2] <= sides[1]:
        return False
    else:
        return True
        


def equilateral(sides):
    if is_triangle(sides) == True and (sides[0] == sides[1] == sides[2]):
        return True
    else:
        return False

def isosceles(sides):
    if is_triangle(sides) == True and (sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]):
        return True
    else:
        return False


def scalene(sides):
    if is_triangle(sides) == True and (sides[0] != sides[1] != sides[2] != sides[0]):
        return True
    else:
        return False
