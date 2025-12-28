alphabets = "abcdefghijklmnopqrstuvwxyz"
sentence = "the 1 quick brown fox jumps over the 2 lazy dogs"

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

print(is_pangram)
