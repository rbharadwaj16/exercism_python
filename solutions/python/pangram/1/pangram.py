def is_pangram(sentence):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    result = ""

    for char in sentence:
        if char.isalpha():
            result += char

    result_lower = result.lower()


    checklist = []

    for alphabet in alphabets:
        if alphabet in result_lower:
            checklist.append(True)
        else:
            checklist.append(False)
    
    is_pangram = all(checklist)

    return (is_pangram)
