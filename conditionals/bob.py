hey_bob = "UPPERCASE LETTERS ?"


def is_question(hey_bob):
    if hey_bob.strip().endswith("?"):
        return True
    else:
        return False
    
def is_capital(hey_bob):
    # Check if the string has letters and all letters are uppercase
    if hey_bob.isupper() and any(c.isalpha() for c in hey_bob):
        return True
    else:
        return False

def is_question_and_capital(hey_bob):
    if is_question(hey_bob) and is_capital(hey_bob):
        return True
    else:
        return False
    

def is_silence(hey_bob):
    if hey_bob == "":
        return True
    elif hey_bob.isspace():
        return True
    else:
        return False
    

def response(hey_bob):
    if is_silence(hey_bob) == True:
        return "Fine. Be that way!"
    elif (is_question(hey_bob) == True) and (is_capital(hey_bob) == True):
        return "Calm down, I know what I'm doing!"
    elif is_question(hey_bob) == True:
        return "Sure."
    elif is_capital(hey_bob) == True:
        return "Whoa, chill out!"
    else:
        return "Whatever."

print(response(hey_bob))