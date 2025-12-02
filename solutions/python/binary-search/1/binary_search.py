def find(search_list, value):

    sorted_list = sorted(search_list)
    lowest_index = 0
    highest_index = len(sorted_list) - 1

    while lowest_index <= highest_index:
        middle_index = (lowest_index + highest_index) // 2
        if sorted_list[middle_index] == value:
            return middle_index
        elif sorted_list[middle_index] > value:
            highest_index = middle_index - 1
        else:
            sorted_list[middle_index] < value
            lowest_index = middle_index + 1
    raise ValueError("value not in array")
