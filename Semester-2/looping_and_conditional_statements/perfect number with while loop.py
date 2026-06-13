num = int(input("Enter a number: "))

i = 1
total = 0

while i < num:   
    if num % i == 0:
        total = total + i
    i = i + 1

if total == num:
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number>")

    

