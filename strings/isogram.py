x = "isogram"


def is_isogram(x):
    for i in x:
        if x.count(i) > 1:
            print(i) 


# def is_isogram(x):
#     for i in x:
#         if x.find(i) == -1:
#             return True
#         else:
#             return False
        


print(is_isogram(x))
