
number = 2
processing_list = []

if number < 1:
    raise ValueError("Classification is only possible for positive integers.")

else:
    for i in range(number):
        if i !=0 and (int(number % i) == 0):
            processing_list.append(i)

    final_sum = sum(processing_list)

    if final_sum == number:
        print("perfect")
    elif number < final_sum:
        print("abundant")
    else:
        print("deficient")
        



