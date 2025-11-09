hey_bob = "UPPERCASE LETTERS"


def is_yell(hey_bob):
    for chars in hey_bob:
        if (chars.isalpha() and chars.isupper()):
            print(True)
        else:
            print(False)


is_yell(hey_bob)