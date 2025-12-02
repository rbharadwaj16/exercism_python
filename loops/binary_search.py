search_list = [4, 8, 12, 14, 20]
value = 15

sorted_list = sorted(search_list)


def binary_search(sorted_list, value):
    lowest_index = 0
    highest_index = len(sorted_list) - 1

    while lowest_index <= highest_index:
        middle_index = (lowest_index + highest_index) // 2
        if sorted_list[middle_index] == value:
            return middle_index
        elif sorted_list[middle_index] > value:
            highest_index = middle_index - 1
        elif sorted_list[middle_index] < value:
            lowest_index = middle_index + 1
        else:
            raise ValueError("value not in array")
        

print(binary_search(sorted_list, value))

