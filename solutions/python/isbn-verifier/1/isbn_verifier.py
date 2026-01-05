def is_valid(isbn):

    custom_list = []
    count = 10
    result = 0

    for i in isbn:
        if i == "X" and isbn[-1] == "X":
            custom_list.append(10)

        elif i.isalpha():
            return (False)

        elif i.isdigit():
            custom_list.append(int(i))

    if len(custom_list) == 10:
        for index, key in enumerate(custom_list):
            result += key * (count - index)

        mod_check = result % 11

        if mod_check == 0:
            return (True)
        else:
            return (False)
    else:
        return(False)
