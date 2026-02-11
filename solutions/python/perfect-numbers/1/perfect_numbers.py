def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    processing_list = []
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    
    else:
        for i in range(number):
            if i !=0 and (int(number % i) == 0):
                processing_list.append(i)
    
        final_sum = sum(processing_list)
    
        if final_sum == number:
            return ("perfect")
        elif number < final_sum:
            return ("abundant")
        else:
            return ("deficient")