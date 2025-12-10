def rotate(text, key):

    str = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for letter in text:
        if letter == " ":
            result += letter
        elif letter.lower() in str:
            initial_index = str.index(letter.lower())
            rotated_char = str[(initial_index + key) % len(str)]
            if letter.isupper():
                result += rotated_char.upper()
            else:
                result += rotated_char
        else:
            result += letter

    return(result)