ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letter = "D"


n = ALPHABETS.index(letter)


top = []

for i in range(n + 1):
    ch = ALPHABETS[i]
    outer = " " * (n - i)

    if i == 0:
        line = outer + ch + outer
    else:
        inner = " " * (2*i - 1)
        line = outer + ch + inner + ch + outer

    top.append(line)

bottom = top[-2::-1]



print(top + bottom)