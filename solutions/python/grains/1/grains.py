def good_numb(number):
    if (number >= 1 and number <=64):
        return True
    else:
        return False

def square(number):
  if good_numb(number) == True:
      x = (number - 1)
      return (2 ** x)
  else:
      raise ValueError("square must be between 1 and 64")


def total():
    return ((2 ** 64) - 1)
