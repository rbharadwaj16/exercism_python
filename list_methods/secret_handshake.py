binary_str = "00011"

a = []

for i in binary_str:
    a.append(i)

b = []
if a[-1] == "1":
    b.append("wink!")
if a[-2] == "1":
    b.append("double blink!")
if a[-3] == "1":
    b.append("close your eyes!")
if a[-4] == "1":
    b.append("jump!")
if a[0] == "1":
    b.reverse()

print(b)
