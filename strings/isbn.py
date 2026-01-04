isbn = "3-598-21508-8"

custom_list = []
count = 10
result = 0

for i in isbn:
    if i.isdigit():
        custom_list.append(i)

for key, index in enumerate(custom_list):
    result += key * (index + count)
    count = count - 1

print(result)