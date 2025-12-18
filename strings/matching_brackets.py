def is_paired(input_string):
    stack = []
    opening = "([{"
    closing = ")]}"
    pairs = {"(": ")", "[": "]", "{": "}"}
    
    for char in input_string:
        if char in opening:
            # Push opening bracket
            stack.append(char)
        elif char in closing:
            # Check if it matches
            if not stack:  # No opening bracket to match
                return False
            last_opening = stack.pop()
            if pairs[last_opening] != char:  # Mismatch
                return False
    
    # Stack should be empty (all brackets closed)
    return len(stack) == 0
