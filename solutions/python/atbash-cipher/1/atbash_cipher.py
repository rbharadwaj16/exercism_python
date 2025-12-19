plain = "abcdefghijklmnopqrstuvwxyz"
cipher = "zyxwvutsrqponmlkjihgfedcba"
CHUNK_SIZE = 5


def encode(plain_text):
    translation_table = str.maketrans(plain, cipher)
    cleaned_text = ""
    for character in plain_text.lower():
        if character.isalnum():
            cleaned_text += character
    encoded_text = cleaned_text.translate(translation_table)
    chunks = []
    for start_index in range(0, len(encoded_text), CHUNK_SIZE):
        end_index = start_index + CHUNK_SIZE
        chunk = encoded_text[start_index:end_index]
        chunks.append(chunk)
    formatted_output = ' '.join(chunks)   
    return formatted_output


def decode(ciphered_text):
    translation_table = str.maketrans(cipher, plain)    
    text_without_spaces = ""
    for character in ciphered_text:
        if character != ' ':
            text_without_spaces += character
    decoded_text = text_without_spaces.translate(translation_table)   
    return decoded_text