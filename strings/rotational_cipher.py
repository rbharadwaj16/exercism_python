str = "abcdefghijklmnopqrstuvwxyz"
key = 5
text = "omg"


for letters in text:
  for index, letter in enumerate(str):
        if letter == text:
         print(str[index + key])