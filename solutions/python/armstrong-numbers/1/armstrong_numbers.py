def is_armstrong_number(number):
    counter = len(str(number))
    x = []
    for i in str(number):
        power = (int(i) ** counter)
        x.append(int(power))
    final = sum(x)
    if final == number:
        return True
    else:
        return False
