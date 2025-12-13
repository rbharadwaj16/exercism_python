
word = "diaper"
candidates = ["hello", "world", "zombies", "pants"]

result = []

for candidate in candidates:
    if len(word) == len(candidate) and candidate.lower() != word.lower():
        if sorted(word.lower()) == sorted(candidate.lower()):
            result.append(candidate)

print(result)
