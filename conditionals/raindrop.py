number = 1

if (number % 3 == 0) and (number % 5 == 0) and (number % 7 == 0):
    print("PlingPlangPlong")
elif (number % 3 == 0) and (number % 5 == 0):
    print("PlingPlang")
elif (number % 5 == 0) and (number % 7 == 0):
    print("PlangPlong")
elif (number % 3 == 0) and (number % 7 == 0):
    print("PlingPlong")
elif (number % 3 == 0):
    print("Pling")
elif (number % 5 == 0):
    print("Plang")
elif (number % 7 == 0):
    print("Plong")
else:
    print (str(number))