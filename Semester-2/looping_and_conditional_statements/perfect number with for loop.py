num = int(input("Enter a number: "))

fact = 0
for i in range (1,num,1):
    if (num % i == 0):
        fact = fact + i

if (num == fact):
    print(f"{num} is a perfect number.")

else:
    print(f"{num} is not a perfect number.")
