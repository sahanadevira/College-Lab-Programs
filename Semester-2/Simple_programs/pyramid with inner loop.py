rows = int(input("Enter number of rows: "))

for i in range (1, rows + 1):
    letter = chr(64+i)
    for j in range(1, i +1):
        print(letter, end = " ")
    print()
