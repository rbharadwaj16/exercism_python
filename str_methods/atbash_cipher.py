"""
Atbash Cipher Implementation

The Atbash cipher is a simple substitution cipher where:
- 'a' maps to 'z', 'b' maps to 'y', 'c' maps to 'x', etc.
- Each letter is replaced with its reverse counterpart in the alphabet
"""

# Define the alphabet mapping for Atbash cipher
PLAIN_ALPHABET = "abcdefghijklmnopqrstuvwxyz"
CIPHER_ALPHABET = "zyxwvutsrqponmlkjihgfedcba"

# Constants for output formatting
CHUNK_SIZE = 5  # Group encoded characters into blocks of 5

def encode(plain_text):
    """
    Encode plain text using the Atbash cipher.
    
    Steps:
    1. Clean the input (lowercase, keep only alphanumeric)
    2. Apply the Atbash substitution cipher
    3. Format the output in groups of 5 characters
    
    Args:
        plain_text: The text to encode
        
    Returns:
        Encoded text grouped in blocks of 5, separated by spaces
    """
    
    # Step 1: Create the translation table for character substitution
    translation_table = str.maketrans(PLAIN_ALPHABET, CIPHER_ALPHABET)
    
    # Step 2: Clean the input text
    # - Convert to lowercase
    # - Keep only alphanumeric characters (letters and digits)
    # - Remove spaces, punctuation, and special characters
    cleaned_text = ""
    for character in plain_text.lower():
        if character.isalnum():
            cleaned_text += character
    
    # Step 3: Apply the Atbash cipher substitution
    # Numbers remain unchanged, only letters are translated
    encoded_text = cleaned_text.translate(translation_table)
    
    # Step 4: Group the encoded text into chunks of 5 characters
    # Create list to hold each chunk
    chunks = []
    for start_index in range(0, len(encoded_text), CHUNK_SIZE):
        end_index = start_index + CHUNK_SIZE
        chunk = encoded_text[start_index:end_index]
        chunks.append(chunk)

    
# Step 5: Join all chunks with spaces
    formatted_output = ' '.join(chunks)
    
    return formatted_output


def decode(encoded_text):
    """
    Decode cipher text using the Atbash cipher.
    
    The Atbash cipher is symmetric - applying it twice gives back the original.
    So decoding uses the same substitution as encoding.
    
    Steps:
    1. Remove spaces from the encoded text
    2. Apply the Atbash substitution cipher (same as encoding)
    3. Return the decoded plain text
    
    Args:
        encoded_text: The cipher text to decode (may contain spaces)
        
    Returns:
        Decoded plain text (no spaces)
    """
    
    # Step 1: Create the translation table (same as encoding - Atbash is symmetric)
    # In Atbash: a→z, z→a, so applying it twice gives back the original
    translation_table = str.maketrans(CIPHER_ALPHABET, PLAIN_ALPHABET)
    
    # Step 2: Remove spaces from the encoded text
    # The encoded text is in groups of 5, we need to combine them
    text_without_spaces = ""
    for character in encoded_text:
        if character != ' ':
            text_without_spaces += character
    
    # Step 3: Apply the Atbash cipher substitution to decode
    # This reverses the encoding
    decoded_text = text_without_spaces.translate(translation_table)
    
    return decoded_text

