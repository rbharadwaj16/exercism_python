def translate(text):
    vowels = "aeiou"
    
    # Split text into words
    words = text.split()
    translated_words = []
    
    for word in words:
        # Rule 1: Vowel start, "xr", or "yt"
        if (word[0] in vowels) or (word[:2] == "xr") or (word[:2] == "yt"):
            translated_words.append(word + "ay")
        else:
            # Rules 2, 3, 4: Consonant clusters
            translated = False
            for index, char in enumerate(word):
                # Rule 3: Check for "qu"
                if index < len(word) - 1 and word[index:index+2] == "qu":
                    consonant_cluster = word[:index+2]
                    rest = word[index+2:]
                    translated_words.append(rest + consonant_cluster + "ay")
                    translated = True
                    break
                # Rule 4: Check for "y" after consonants
                elif char == "y" and index > 0:
                    consonant_cluster = word[:index]
                    rest = word[index:]
                    translated_words.append(rest + consonant_cluster + "ay")
                    translated = True
                    break
                # Rule 2: Check for vowel
                elif char in vowels:
                    consonant_cluster = word[:index]
                    rest = word[index:]
                    translated_words.append(rest + consonant_cluster + "ay")
                    translated = True
                    break
            
            # Edge case: no vowels found
            if not translated:
                translated_words.append(word + "ay")
    
    # Join all translated words back together
    return " ".join(translated_words)

