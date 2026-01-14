alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
target = "D"

max_idx = alphabet.find(target)

rows = []
for i in range(max_idx + 1):
    letter = alphabet[i]
    outer_spaces = " " * (max_idx - i)
    if i == 0:
        rows.append(outer_spaces + letter + outer_spaces)
    else:
        inner_spaces = " " * (2 * i - 1)
        rows.append(outer_spaces + letter + inner_spaces + letter + outer_spaces)

# Mirror the rows (excluding the middle row)
for i in range(max_idx - 1, -1, -1):
    rows.append(rows[i])

for row in rows:
    print(f'"{row}",')