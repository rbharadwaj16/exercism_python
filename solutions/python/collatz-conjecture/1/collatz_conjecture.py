def steps(number):

    counter = 0
    
    
    
    def check_even(number):
        if (number % 2 == 0):
            return True
        else:
            return False
    
    def check_odd(number):
        if (number % 2 != 0):
            return True
        else:
            return False
    
    
    
    while (number != 1):
        if (number <=0):
            raise ValueError("Only positive integers are allowed")
        elif check_even(number) == True:
            number = number/2
            counter = counter + 1
        elif check_odd(number) == True:
            number = (number * 3) + 1
            counter = counter + 1

    return counter