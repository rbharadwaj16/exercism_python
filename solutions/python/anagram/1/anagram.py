def find_anagrams(word, candidates):
    result = []

    for candidate in candidates:
        if len(word) == len(candidate) and candidate.lower() != word.lower():
            if sorted(word.lower()) == sorted(candidate.lower()):
                result.append(candidate)
    return result
